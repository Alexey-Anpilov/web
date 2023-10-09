import os
import pika
import sys
from proto_out.users_pb2 import UserAddr, UserName

def main():
    # Подготавливаем channel и exchange, создаем очередь
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='user_info',
                             exchange_type='direct')
    
    result = channel.queue_declare(queue='', exclusive=True)

    queue_name = result.method.queue
    
    # Работаем с аргументами командной строки, связываем очередь и exchange
    severities = sys.argv[1:]

    if not severities:
        sys.stderr.write("Usage: python3 %s [name] [address]\n" % sys.argv[0])
        sys.exit(1)
    
    for severity in severities:
        channel.queue_bind(
            exchange='user_info', queue=queue_name, routing_key=severity
        )

    print(' [*] Waiting for logs. To exit press CTRL+C')

    # Определим callback-функцию и начнем слушать сообщения
    def callback(ch, method, properties, body):
        if method.routing_key == "address":
            msg = UserAddr()
            msg.ParseFromString(body)
            print(f'User address is {msg.addr}')
        elif method.routing_key == "name":
            msg = UserName()
            msg.ParseFromString(body)
            # Тут почему-то вылетает AttributeError при попытке обраться к атрибутам FullName. Не смог понять причину.
            # Вероятно связано с вложенностью сообщения FullName, т.к. с сообщение адреса все ок.
            print(f'User name is {msg.FullName.last_name} {msg.FullName.first_name} {msg.FullName.second_name}')


    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()   


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)