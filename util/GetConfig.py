# -*- coding: utf-8 -*-
import os
from util.utilClass import ConfigParse
from util.utilClass import LazyProperty

class GetConfig(object):
    def __init__(self):
        self.pwd = os.path.split(os.path.realpath(__file__))[0]
        self.config_path = os.path.join(os.path.split(self.pwd)[0], 'Config.ini')
        self.config_file = ConfigParse()
        self.config_file.read(self.config_path)

    @LazyProperty
    def db_type(self):
        return self.config_file.get('DB','type')

    @LazyProperty
    def db_name(self):
        return self.config_file.get('DB','name')

    @LazyProperty
    def db_host(self):
        return self.config_file.get('DB','host')

    @LazyProperty
    def db_port(self):
        return int(self.config_file.get('DB','port'))

    @LazyProperty
    def proxy_getter_functions(self):
        return self.config_file.options('ProxyGetter')

if __name__ == '__main__':
    gc = GetConfig()
    print(gc.db_type)
    print(gc.db_name)
    print(gc.db_host)
    print(gc.db_port)
    print(gc.proxy_getter_functions)