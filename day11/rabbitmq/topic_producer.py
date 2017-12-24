__author__ = 'Cq'

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs1',
                         exchange_type='topic')

#默认发送的消息格式为xxx.info
severity = sys.argv[1] if len(sys.argv) > 1 else 'test_message.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs1',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
