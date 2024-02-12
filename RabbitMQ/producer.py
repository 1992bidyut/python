import pika
import time
credentials = pika.PlainCredentials('guest', 'guest')
connection_parameter =  pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.queue_declare(queue='fttx_boxs')

for step in range(1, 20):
    message = f'(Step:{step}) Hello from fttx_box!'
    channel.basic_publish(exchange='', routing_key='fttx_boxs', body=message)
    time.sleep(2)
    print('Sent message', message, step)



connection.close()