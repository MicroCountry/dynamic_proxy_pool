# -*- coding: utf-8 -*-
import json
import random
import redis

class RedisClient(object):
    def __init__(self,name,host,port):
        self.name = name
        self.__conn = redis.Redis(host=host,port=port,db=0)

    def get(self):
        key = self.__conn.hgetall(name=self.name)
        return random.choice(key.keys()) if key else None

    def put(self,key):
        key = json.dumps(key) if isinstance(key,(dict,list)) else key
        return self.__conn.hincrby(self.name,key,1)

    def getvalue(self,key):
        value = self.__conn.hget(self.name,key)

    def pop(self):
        key = self.get()
        if key:
            self.__conn.hdel(self.name,key)
            return key

    def delete(self,key):
        self.__conn.hdel(self.name, key)

    def inckey(self, key, value):
        self.__conn.hincrby(self.name, key, value)

    def getAll(self):
        return self.__conn.hgetall(self.name).keys()

    def get_status(self):
        return self.__conn.hlen(self.name)

    def changeTable(self,name):
        self.name = name

if __name__ == '__main__':
    redis_con = RedisClient('proxy','localhost',6379)





