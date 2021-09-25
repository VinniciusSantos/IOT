from socket import socket
import socket 

HOST = ''
PORT = 5000

tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#SOCK_STREAM para conexões tcp
origem = (HOST,PORT)
tcp.bind(origem)
tcp.listen(1)#Diz ao protocolo quantas conexões ele vai poder aceitar por vez

print("Servidor TCP em funcionamento! ")

while True:#Loop para aceitar a contexão
    con, cliente = tcp.accept()
    print(f'Conectado com {cliente} na porta {con}')
    while True:#Outro loop para receber a mensagem da conexão aceita
        mensagem = con.recv(1024)
        print(f"Mensagem de {cliente}\nConteúdo: {mensagem}")

con.close()