bloques = int(input("Ingrese el número de bloques:"))
altura=0
nivel=bloques
# Escribe tu código aquí.
while nivel>altura:
    for i in range(1,bloques):
        if nivel>altura:
            nivel-=i
            altura+=1
print("La altura de la pirámide:", altura)