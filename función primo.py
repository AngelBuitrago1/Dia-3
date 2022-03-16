def isPrime(num):
    if num%2!=1:
        return False
    else:
        return True

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()