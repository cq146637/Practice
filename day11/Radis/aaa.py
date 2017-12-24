#对台服务器同时管理一个频道，只要订阅了该频道的订阅者都能收到任意服务器的消息

import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='10.211.55.4')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()      #打开收音机
        pub.subscribe(self.chan_sub)    #调频道
        pub.parse_response()            #准备接收
        return pub



def subscriber():

    obj = RedisHelper()
    redis_sub = obj.subscribe()

    while True:
        msg= redis_sub.parse_response()
        print(msg)


def promulgator():
    obj = RedisHelper()
    obj.public('hello')



def main():
    promulgator()
    subscriber()



if "__main__" == __name__:
    main()