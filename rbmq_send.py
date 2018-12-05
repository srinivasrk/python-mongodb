import pika
import os


def send_message(message_body):
    credentials = pika.PlainCredentials('srini', 'srini')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(os.environ['RABBITMQ_SERVER'], 5672, '/', credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue='tasks', durable=True)

    channel.basic_publish(exchange='',
                          routing_key='tasks',
                          body=message_body,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))

    print(" [x] Sent 'Hello World!'")

    connection.close()
