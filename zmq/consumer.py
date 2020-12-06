import zmq

ctx = zmq.Context()
sock = ctx.socket(zmq.SUB)
sock.connect("tcp://127.0.0.1:1211")
sock.subscribe("") # Subscribe to all topics
print("Starting receiver loop ...")
count=0
while True:
    msg = sock.recv().decode("utf-8")
    #msg = your data

sock.close()
ctx.term()
