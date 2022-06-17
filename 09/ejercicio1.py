paises = input("ingrese paises separador por comas:\n")

paises = paises.split(",")

print(",".join(sorted(list(set(paises)))))