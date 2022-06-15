def es_primo(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

print("5 es primo? " + str(es_primo(5)))
print("8 es primo? " + str(es_primo(8)))