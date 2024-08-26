import csv

# Define o salário
salario = float(input("Qual o valor do seu salário? "))

# Inicializa a variável para acumular o total das contas
total_contas = 0

# Lê os valores das contas do arquivo CSV
with open('exemplo.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        try:
            # Supondo que o valor da conta esteja na primeira coluna
            conta = float(row[1])
            print(row)
            total_contas += conta
        except ValueError:
            print(f"Valor inválido encontrado na linha: {row}")

# Calcula o valor restante após pagar todas as contas
valor_restante = salario - total_contas

# Exibe o resultado
print(f"Total das contas: R${total_contas:.2f}")
print(f"Saldo: R${valor_restante:.2f}")
print("END")
