import os
import platform

def verificar_arquivo_nao_vazio(nome_arquivo):
    return os.path.getsize(nome_arquivo) > 0
