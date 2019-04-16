# 참조: https://blog.storyg.co/rabbitmqs/tutorials/python/02-work-queue

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', routing_key='task_queue',  body=message,
        properties=pika.BasicProperties(
                delivery_mode = 2,
        )
)
print(" [x] Sent %r" % message)

