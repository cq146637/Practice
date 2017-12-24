__author__ = 'Cq'


import memcache

mc = memcache.Client(['192.168.198.128:12000'],debug=True)

mc.set("a1","foo")
mc.set("k1","1")
mc.append('a1', 'after')
mc.prepend('a1', 'before')
mc.incr('k1')
# mc.add("a1","aaa")
# mc.replace("a1","bbb")
mc.set_multi({'key1': 'val1', 'key2': 'val2'})
item_dict = mc.get_multi(["key1", "key2", "key3"])
# mc.delete("key0")
ret = mc.get('k1')
print(ret)