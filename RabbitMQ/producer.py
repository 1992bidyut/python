import pika
import time
credentials = pika.PlainCredentials('bidyut', '1234')
connection_parameter =  pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.queue_declare(queue='tofa_1234')

for step in range(0, 5):
    message = f'(Step:{step}) Hello from fttx_box!'
    channel.basic_publish(exchange='', routing_key='tofa_1234', body=message)
    time.sleep(2)
    print('Sent message', message, step)

connection.close()