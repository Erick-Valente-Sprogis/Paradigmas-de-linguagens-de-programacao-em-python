#Cálculo de Média

nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))

if(nota1+nota2)/2>=5:
  print("Aprovado Primeira Parte\n")
  print((nota1+nota2)/2)

  if(nota1+nota2)/2 >=7:
    print("Aprovado")
    print((nota1+nota2)/2)
  
  else:
    print("Recupeação")
    print((nota1+nota2)/2)
  
else:
  print("Reprovado")
  print((nota1+nota2)/2)

print("END")
