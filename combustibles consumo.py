def l100kmtompg(liters):
    mpg=((100000/1609.344)/(liters/3.785411784))
    return mpg
def mpgtol100km(miles):
    lkm=((miles*1.609344)/3.785411784)
    return (1/lkm)*100
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))