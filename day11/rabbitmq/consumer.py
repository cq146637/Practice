__author__ = 'Cq'

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()


#You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
#was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
#发送方和接收方不知道谁首先连接到RabbitMQ，双方连接上来都先声明一个队列
channel.queue_declare(queue='hello2', durable=True)

def callback(ch, method, properties, body):
    print("recived message...")
    # time.sleep(30)
    print(" [x] Received %r" % body)
    #处理完成消息后，主动要向RabbitMQ发送ack
    ch.basic_ack(delivery_tag=method.delivery_tag)
    #ch -->  管道内存对象的地址
    #method --> 指定各种参数
    #properties -->
    #python3 socket等发送网络包都是byte格式

#如果队列里还有1条消息未处理完，将不能接收新的消息
channel.basic_qos(prefetch_count=1)

#声明接收收消息变量
channel.basic_consume(callback,#收到消息后执行的回调函数
                      queue='hello2',)
                     #no_ack=True)#执行完callback函数后，默认会发送ack给RabbitMQ

print(' [*] Waiting for messages. To exit press CTRL+C')
#开始接收消息，不停循环接收，没有消息挂起等待
channel.start_consuming()
