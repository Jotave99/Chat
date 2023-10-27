import socket;
import datetime;

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

cliente.connect(('localhost', 8888));

data = datetime.date.today();
dataFormatada = data.strftime("%d/%m/%y");

nick = input('Digite o seu nick: ');

terminado = False;
print('Digite tt para terminar o chat');

while not terminado:
    cliente.send(input('['+dataFormatada+'] ['+nick +']: ').encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'sair':
        terminado = True
    else:
        print(msg)

cliente.close();