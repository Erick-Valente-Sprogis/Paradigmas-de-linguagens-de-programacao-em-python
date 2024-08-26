  # Define o salário
salario = 2500

  # Inicializa a variável para acumular o total das contas
total_contas = 0

  # Pergunta ao usuário quantas contas ele deseja informar
quantidade_de_contas = int(input("Quantas contas você deseja informar? "))

  # Loop para coletar os valores das contas
for i in range(quantidade_de_contas):
    conta = float(input(f"Digite o valor da conta {i+1}: "))
    total_contas += conta

  # Calcula o valor restante após pagar todas as contas
valor_restante = salario - total_contas

  # Exibe o resultado
print(f"Total das contas: R${total_contas:.2f}")
print(f"Saldo: R${valor_restante:.2f}")
