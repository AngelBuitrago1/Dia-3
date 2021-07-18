palabraSinVocal = ""
print('ingrese una palabra: ')
userWord=str(input())
userWord = userWord.upper()

for letra in userWord:
    if letra=='A':
        continue
    elif letra=='E':
        continue
    elif letra=='I':
        continue
    elif letra=='O':
        continue
    elif letra=='U':
        continue
    else:
        palabraSinVocal = letra
    print(palabraSinVocal, end='')