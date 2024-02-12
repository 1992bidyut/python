import pika

def on_message_received(ch, method, properties, body):
    print(f'Received message {body}')
    
def callback(ch, method, properties, body):
    print("Received message:", body.decode())

credentials = pika.PlainCredentials('bidyut', '1234')
connection_parameter =  pika.ConnectionParameters('192.168.10.177', 5672, '/', credentials)

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

# get message by que
channel.queue_declare(queue='tofa_1234')
channel.basic_consume(queue='tofa_1234', auto_ack=True, on_message_callback=on_message_received,)

# get message by exchange
# exchange_name = 'tofa_1234'
# channel.exchange_declare(exchange=exchange_name, exchange_type='topic')
# result = channel.queue_declare(queue='', exclusive=True)
# queue_name = result.method.queue
# channel.queue_bind(exchange=exchange_name, queue=queue_name)
# channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)


print('Starting consuming')
channel.start_consuming()