from http.client import HTTPConnection
#de httpcliente importe HttpConnection

conexao = HTTPConnection('localhost', 5000)
conexao.request('GET',"/")
resposta = conexao.getresponse()
pagina = resposta.read()

print(pagina)