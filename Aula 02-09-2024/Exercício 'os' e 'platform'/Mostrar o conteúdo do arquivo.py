import os
import platform

def mostrar_conteudo_arquivo(nome_arquivo):
    if verificar_existe_arquivo(nome_arquivo) and verificar_arquivo_nao_vazio(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read()
    else:
        return "O arquivo não existe ou está vazio."
