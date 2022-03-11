ingreso=float(input("Ingrese el ingreso anual:"))

#
# Coloca tu código aquí.
#
if (ingreso <=0):
    impuesto=0.0
elif (ingreso>0 and ingreso<=85528):
    impuesto=(ingreso*.18)-566.2
    if impuesto<0:
        impuesto=0.0
else:
    impuesto=14839.2+((ingreso-85528)*.32)
impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
