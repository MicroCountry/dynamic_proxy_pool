# -*- coding: utf-8 -*-
from db.DbClient import DbClient
from util.GetConfig import GetConfig
from util.LogHandler import LogHandler
from proxyGetter.GetFreeProxy import GeteFreeProxy

class ProxyManager(object):
    def __init__(self):
        self.db = DbClient()
        self.config = GetConfig()
        self.raw_proxy_queue = 'raw_proxy'
        self.log = LogHandler('proxy_manager')
        self.useful_proxy_queue = 'useful_proxy'

    def refresh(self):
        for proxyGetter in self.config.proxy_getter_functions:
            proxy_set = set()
            for proxy in getattr(GeteFreeProxy,proxyGetter.strip())():
                if proxy.strip():
                    self.log.info('{func}: fetch proxy {proxy}'.format(func=proxyGetter, proxy=proxy))
                    proxy_set.add(proxy.strip())

            self.db.changeTable(self.raw_proxy_queue)
            for proxy in proxy_set:
                self.db.put(proxy)

    def get(self):
        self.db.changeTable(self.useful_proxy_queue)
        return self.db.get()

    def delete(self,proxy):
        self.db.changeTable(self.useful_proxy_queue)
        self.db.delete(proxy)

    def getAll(self):
        self.db.changeTable(self.useful_proxy_queue)
        return self.db.getAll()

    def get_status(self):
        self.db.changeTable(self.raw_proxy_queue)
        total_raw_proxy = self.db.get_status()
        self.db.changeTable(self.useful_proxy_queue)
        total_useful_queue = self.db.get_status()
        return {'raw_proxy': total_raw_proxy, 'useful_proxy': total_useful_queue}

if __name__ == '__main__':
    pp = ProxyManager()
    pp.refresh()
    print(pp.get_status())