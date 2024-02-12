import pika

def on_message_received(ch, method, properties, body):
    print(f'Received message {body}')

credentials = pika.PlainCredentials('guest', 'guest')
connection_parameter =  pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.queue_declare(queue='fttx_boxs')

channel.basic_consume(queue='fttx_boxs', auto_ack=True, on_message_callback=on_message_received)

print('Starting consuming')

channel.start_consuming()