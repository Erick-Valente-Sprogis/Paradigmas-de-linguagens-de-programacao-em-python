#sensor de temperatura

num1 = float(input("Primeiro Sensor: "))
num2 = float(input("Segundo Sensor: "))
media = (num1 + num2) / 2

if (num1 + num2) / 2 >= 30:
  print("Está quente")

elif (num1 + num2) / 2 >= 20:
  print("Um pouco quente")

elif (num1 + num2) / 2 >= 10:
  print("Um pouco frio")
  
else:
  print("Está frio")
print(media)
print("END")
