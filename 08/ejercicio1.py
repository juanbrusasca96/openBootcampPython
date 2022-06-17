file = open('prueba.txt', 'w')
file.write("Primera línea\n")
file.close()

file = open('prueba.txt', 'r+')
file.readline()
file.write('Segunda linea')

print(file.read())
file.close()