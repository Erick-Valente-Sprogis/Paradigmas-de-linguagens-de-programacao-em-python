nomes = ['N0', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6']

'''
for n in nomes:
  print(n)
'''

cont = 0 #inicializa o contador com zero/0
for value in range(cont,7):
  print(nomes[value], end=',')
  if (cont % 2 == 1):
    print('')
cont = cont + 1
