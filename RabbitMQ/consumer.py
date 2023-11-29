import pika

def on_message_received(ch, method, properties, body):
    print(f'Received message {body}')

connection_parameter =  pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.queue_declare(queue='fttx_box')

channel.basic_consume(queue='fttx_box', auto_ack=True, on_message_callback=on_message_received)

print('Starting consuming')

channel.start_consuming()