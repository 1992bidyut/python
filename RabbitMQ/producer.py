import pika
import time

connection_parameter =  pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.queue_declare(queue='fttx_box')

for step in range(1, 20):
    message = f'(Step:{step}) Hello from fttx_box!'
    channel.basic_publish(exchange='', routing_key='fttx_box', body=message)
    time.sleep(2)
    print('Sent message', message, step)



connection.close()