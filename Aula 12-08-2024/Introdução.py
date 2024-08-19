print("Hello Wold!")
print("Primeira Aula\n")

mensagem = "Exemplo de mensagem"
n = 25
pi = 3.141592653589793238462643383279502884197169399375
print(mensagem)
print(n)
print(pi)
print(n + n)



print("\n\nAcesso ao Sistema")
login = input("Usuário: ")
senha = input("Senha: ")
print("\nUsuário: " + login + "\nSenha: " + senha)
print("\nLogin: %s, Senha: %s" % (login, senha))



v1 = int(input("\n\nValor1: "))
v2 = int(input("Valor2: "))
print("Soma: %s" % (v1 + v2))



v3 = int(input("\n\nValor3: "))
v4 = int(input("Valor4: "))
print("\nA soma de %s e %s é igual a %s" % (v3, v4, v3 + v4))
if v3==v4:
  print("\nOs valores são iguais")
else:
  print("\nOs valores são diferentes")
