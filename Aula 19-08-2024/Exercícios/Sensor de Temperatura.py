#sensor de temperatura

num1 = float(input("Primeiro Sensor: "))
num2 = float(input("Segundo Sensor: "))

if(num1+num2)/2 >= 30:
  print("Está quente")
  print((num1+num2)/2)
  
elif(num1+num2)/2 >= 20:
  print("Um pouco quente")
  print((num1+num2)/2)
  
elif(num1+num2)/2 >= 10:
  print("Um pouco frio")
  print((num1+num2)/2)
  
else:
  print("Está frio")
  print((num1+num2)/2)
print("END")
