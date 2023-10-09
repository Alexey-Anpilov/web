'''
    Sender может отправить один из двух типов сообщений - имя пользователя или адрес. Необходимо указать соответствующий routing_key.
    Reciever может получать оба типа сообщений. Reciever создает очередь и привязывает ее к exchange с соответствующим routing key.
'''
import pika
import sys
from proto_out.users_pb2 import UserName, UserAddr

# Подготавливаем channel и exchange
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='user_info',
                         exchange_type='direct'
                         )

# Работаем с аргументами командной строки и формируем сообщение
if len(sys.argv) < 1:
    sys.stderr.write("Specify severity and user information.\n Usage: python3 %s [name] [address] [user_info]\n")
    sys.exit(1)

severity, user_info = sys.argv[1], sys.argv[2:]

if severity == 'name':
    name = sys.argv[2:]
    message = UserName(name=UserName.FullName(second_name=name[0], 
                                              first_name=name[1],
                                              last_name=name[2]))   
elif severity == 'address':
    message = UserAddr(addr=' '.join(sys.argv[2:]))
else:
    sys.stderr.write("Invalid severity.\n")
    sys.exit(1)

message = message.SerializeToString()

# Отправляем сообщение в очередь
channel.basic_publish(
    exchange='user_info', routing_key=severity, body=message)

connection.close()