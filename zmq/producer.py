import zmq
import time
import json
from faker import Faker

ctx = zmq.Context()
sock = ctx.socket(zmq.PUB)
sock.bind("tcp://*:1211")
msg={"Name":"Milan Bhardwaj","Job": "Development Engineer", "Website":"Medium"}

while True:
    sock.send_string(str(msg))

sock.close()
ctx.term()