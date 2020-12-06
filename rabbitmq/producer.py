#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
msg={"Name":"Milan Bhardwaj","Job": "Development Engineer", "Website":"Medium"}

while True:
    channel.basic_publish(exchange='', routing_key='hello', body=str(msg))

connection.close()