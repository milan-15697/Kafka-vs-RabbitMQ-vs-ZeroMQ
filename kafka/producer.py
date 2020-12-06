from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'mybroker1,mybroker2'})

while True:
    p.poll(0)
    p.produce('mytopic', data.encode('utf-8'))

p.flush()