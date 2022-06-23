import os
import time

def clean():
    os.system("cls")

def mimir():
   time.sleep(2)

def registro():
    try:
        arquivo = open("registro_de_login.txt", "r")
        conteudo = arquivo.read()
        arquivo.close()
        return conteudo
    except:
        arquivo = open("registro_de_login.txt", "w")
        arquivo.close()
        return ""