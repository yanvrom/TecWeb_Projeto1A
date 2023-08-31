import json
import codecs
from database import Database, Note

db = Database('notes')

def extract_route(requisicao:str):
    rota = requisicao.split()[1][1:]
    return rota

def read_file(path):
    conteudo = open(path, "r+b").read()
    return conteudo

def load_data():
    notas = db.get_all()
    return notas

def load_template(nome_arquivo_template):
    template = open("templates/"+nome_arquivo_template, "r", encoding = "utf-8").read()
    return template

def add_anotacao(titulo, detalhes):
    nota = Note(title=titulo, content=detalhes)
    db.add(nota)
    
def build_response(body='', code=200, reason='OK', headers=''):
    'HTTP/1.1 200 OK\n\n'
    if headers == '':
        retornar = 'HTTP/1.1 ' + str(code) + ' ' + reason + '\n\n' + body
    else:
        retornar = 'HTTP/1.1 ' + str(code) + ' ' + reason + '\n' + headers + '\n\n' + body
    return retornar.encode()