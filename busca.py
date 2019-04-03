#coding: utf-8
import socket

class whois:
    def __init__(self, query):
        self.query = query
    def obtem_identificacao(self):
        destino = ('200.160.2.3',43)
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.connect(destino)
        tcp.send(self.query.encode())
        dados = tcp.recv(1024)
        tcp.close()
        dados = dados.decode('utf-8', 'backslashreplace')
        try:
            return print('ownerid:{}'.format(dados.split()[dados.split().index('ownerid:')+1]))
        except:
            return print('Query inválida ou ownerid inexistente')

