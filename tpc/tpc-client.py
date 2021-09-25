import socket

HOST = 'localhost'
PORT = 5000

tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

destino = (HOST,PORT)

while True:
    mensagem = bytes(input("Digite uma mensagem: "), encoding = 'utf-8')
    tcp.send(mensagem)

tpc.close
