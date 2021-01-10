import pika

params = pika.URLParameters('amqps://ygcishzz:g5OvXmghiHlAbTR4r64d3tqcu14Hfcba@gerbil.rmq.cloudamqp.com/ygcishzz')

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print('Start consuming')

channel.start_consuming()
channel.close()
