import time

time = time.localtime()
hora = time.tm_hour
minutos = time.tm_min
segundos = time.tm_sec
falta = "faltan " + str(19-(hora+1)) + ":" + str(60-minutos) + ":" + str(60-segundos) + " para ir a casa"
if hora>19:
    print("ya es hora de ir a casa")
else:
    print(falta)