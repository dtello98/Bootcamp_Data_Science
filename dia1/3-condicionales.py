numero1 = int(input("Ingrese el primer numero "))
numero2 = int(input("Ingrese el primer numero "))
operacion = input("Ingrese la operacion a realizar (+,-,/,*)")

if operacion == "+":
    resultado=numero1+numero2
elif operacion == "-":
    resultado=numero1-numero2
elif operacion == "*":
    resultado=numero1*numero2
elif operacion == "/":
    resultado=numero1/numero2
else:
    print("Operacion no valida")

print("El resultado es ", resultado)