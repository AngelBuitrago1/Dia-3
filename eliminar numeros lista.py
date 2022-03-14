miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
list=[]
for numero in miLista:
    if numero not in list:
        list.append(numero)
        miLista=list
print("La lista solo con elementos únicos:")
print(miLista)