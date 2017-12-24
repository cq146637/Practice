import redis
 
pool = redis.ConnectionPool(host="192.168.198.128", port='6379',password=123456)
 
r = redis.Redis(connection_pool=pool)
 
# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)
 
pipe.set('name', 'alex')
pipe.set('role', 'sb')
 
pipe.execute()