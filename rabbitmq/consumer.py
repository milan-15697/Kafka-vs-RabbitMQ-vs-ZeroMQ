#!/usr/bin/env python

import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
count=0

def callback(ch, method, properties, body):
    #body = your message

channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)
channel.start_consuming()