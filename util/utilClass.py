# -*- coding: utf-8 -*-
class LazyProperty(object):
    def __init__(self,func):
        self.func = func
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance,self.func.__name__,value)
            return value

from ConfigParser import ConfigParser

class ConfigParse(ConfigParser):
    def __init__(self):
        ConfigParser.__init__(self)

    def optionxform(self, optionstr):
        return optionstr

class Singleton(type):
    _inst={}
    def __call__(self, *args, **kwargs):
        if self not in self._inst:
            self._inst[self] = super(Singleton,self).__call__(*args)
        return self._inst[self]