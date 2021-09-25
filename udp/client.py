import socket as sk

HOST = 'localhost' #127.0.0.1
PORT = 5000

udp = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
destino = (HOST,PORT)

#msg = input("Digite a mensagem: ")

while(True):

    mensagem = bytes(input("Digite uma mensagem: "), encoding = 'utf-8')

    if mensagem == bytes('sair', encoding = 'utf-8'):
        exit()
    else:
        udp.sendto(mensagem,destino)
    
udp.close()