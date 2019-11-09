import asyncio

while True:
    file=open('server.log','a')
    HOST = input('Введите адрес хоста или localhost:\n')
    file.write("Запрашиваю адрес хоста...\n")
    if HOST=='localhost':
        HOST='127.0.0.1'
        file.write(f"введенный адрес хоста: {HOST} \n")
        file.close()
        break
    if HOST=='':
        file.write("адрес хоста не установлен. \n")
        file.close()
        break
    host_l=HOST.split('.')
    if (0<=int(host_l[0])<255) and (0<=int(host_l[1])<255) and (0<=int(host_l[2])<255) and (0<=int(host_l[3])<255):
        file.write(f"Введенный адрес хоста: {HOST} \n")
        file.close()
        break
    else:
        print('Введен неверный формат адреса.')
        file.write("Введен неверный адрес хоста, запрашиваю адрес снова.\n")


while True:
    file=open('server.log','a')
    PORT=input('Введите номер порта от 1024 до 49151: \n')
    PORT=int(PORT)
    file.write("Запрашиваю номер порта...\n")
    if 1023<PORT<49152:
        file.write(f"введенный номер порта: {PORT} \n")
        file.close()
        break
    else:
        print('Неверный номер порта.')
        file.write("введен неверный номер порта, запрашиваю номер снова...\n")

async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection(HOST,PORT,loop=loop)
    writer.write(message.encode())
    data=await reader.read(100)
    print(f'Отправлено: {data.decode()}')
    print('Закрыл соединение')
    writer.close()

message='Hello World!'
loop=asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message,loop))
loop.close()