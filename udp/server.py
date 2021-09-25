import socket as sk

HOST = ''
PORT = 5000 
#A porta udp que vai ser aberta para aceitar conexão externa

print(f"O host é {HOST} e a porta é {PORT}\n")

udp = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)#Tipo de socket / ipv4 conexão udp
#Sock_Dgram = conexões udp
#Sock_Stream = conexões tcp
origem = (HOST,PORT)#será utilizado para inserir as informações no socket
udp.bind(origem)#Informações inseridas no socket

print("Servidor UDP iniciado\n")

while True:
    
    msg, cliente = udp.recvfrom(1024)
    if msg == bytes('desligar servidor', encoding = 'utf-8'):
        print('Servidor desligando')
        exit(0)
    else:
        print(f"A mensagem do cliente {cliente} contém o conteudo \n'{msg}'")

udp.close()