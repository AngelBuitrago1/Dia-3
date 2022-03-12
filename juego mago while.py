numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
n=int(input(": "))
while n!=numeroSecreto:
    print("\"¡Ja, ja! ¡Estás atrapado en mi ciclo!\"\n Ingresa otro número")
    n=int(input(": "))
print(n, "\"¡Bien hecho, muggle! Eres libre ahora\"")
    