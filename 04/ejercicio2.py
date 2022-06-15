numero_inicial = input("ingrese el numero inicial ")
numero_final=input("ingrese el numero final ")
numero_inicial = int(numero_inicial)
numero_final = int(numero_final)
while numero_inicial<numero_final:
    if numero_inicial%2!=0:
        print(numero_inicial)
    numero_inicial+=1
