import pika

params = pika.URLParameters('amqps://ygcishzz:g5OvXmghiHlAbTR4r64d3tqcu14Hfcba@gerbil.rmq.cloudamqp.com/ygcishzz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')