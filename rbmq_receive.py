import pika
import os
import time

def receive_message():
    credentials = pika.PlainCredentials('srini', 'srini')
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['RABBITMQ_SERVER'], 5672, '/', credentials))
    channel = connection.channel()

    channel.queue_declare(queue='tasks', durable=True)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        time.sleep(2)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Fair dispatch
    channel.basic_qos(prefetch_count=1)

    # send ack
    channel.basic_consume(callback,
                          queue='tasks')

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


receive_message()
