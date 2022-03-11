hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
a=min+dura
b=a//60
c=a%60
hora += b
hora=hora%24
print("salida esperada: "+str(hora)+':'+str(c))