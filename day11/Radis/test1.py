__author__ = 'Cq'

import redis

r = redis.Redis(host="192.168.198.128", port='6379',password=123456)
r.set(name="k1", value="aaa")
res = r.incrbyfloat(name="name")
print(res)