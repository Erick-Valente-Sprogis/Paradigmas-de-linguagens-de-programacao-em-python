import os
import platform


def verificar_existe_arquivo(nome_arquivo):  #verificar_existe_arquivo
  return os.path.exists(nome_arquivo)


def verificar_arquivo_nao_vazio(nome_arquivo):  #verificar_arquivo_nao_vazio
  return os.path.getsize(nome_arquivo) > 0


def mostrar_conteudo_arquivo(nome_arquivo):  #mostrar_conteudo_arquivo
  if verificar_existe_arquivo(nome_arquivo) and verificar_arquivo_nao_vazio(
      nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
      return arquivo.read()
  else:
    return "O arquivo não existe ou está vazio."


def contar_linhas_arquivo(nome_arquivo):  #contar_linhas_arquivo
  if verificar_existe_arquivo(nome_arquivo) and verificar_arquivo_nao_vazio(
      nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
      return sum(1 for _ in arquivo)
  else:
    return "O arquivo não existe ou está vazio."


nome_arquivo = 'exemplo.csv'

# Verifica se o arquivo existe
print(
    verificar_existe_arquivo(nome_arquivo))  # Exemplo de saída: True ou False

# Verifica se o arquivo não está vazio
print(verificar_arquivo_nao_vazio(
    nome_arquivo))  # Exemplo de saída: True ou False

# Mostra o conteúdo do arquivo
print(mostrar_conteudo_arquivo(
    nome_arquivo))  # Exemplo de saída: conteúdo do arquivo ou mensagem de erro

# Conta a quantidade de linhas do arquivo
print(contar_linhas_arquivo(
    nome_arquivo))  # Exemplo de saída: número de linhas ou mensagem de erro
