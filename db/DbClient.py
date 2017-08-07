# -*- coding: utf-8 -*-
import os
import sys

from util.GetConfig import GetConfig
from util.utilClass import Singleton

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class DbClient(object):

    __metaclass__ = Singleton

    def __init__(self):
        self.config = GetConfig()
        self.__initDbClient()

    def __initDbClient(self):
        __type = "RedisClient"
        self.client = getattr(__import__(__type), __type)(name=self.config.db_name,
                                  host=self.config.db_host,
                                  port=self.config.db_port)

    def get(self, **kwargs):
        return self.client.get(**kwargs)

    def put(self, key, **kwargs):
        return self.client.put(key, **kwargs)

    def getvalue(self, key, **kwargs):
        return self.client.getvalue(key, **kwargs)

    def pop(self, **kwargs):
        return self.client.pop(**kwargs)

    def inckey(self, key, value, **kwargs):
        return self.client.inckey(key, value, **kwargs)

    def delete(self, key, **kwargs):
        return self.client.delete(key, **kwargs)

    def getAll(self):
        return self.client.getAll()

    def changeTable(self, name):
        self.client.changeTable(name)

    def get_status(self):
        return self.client.get_status()


if __name__ == "__main__":
    account = DbClient()
    print(account.get())
    account.changeTable('use')
    account.put('ac')
    print(account.get())