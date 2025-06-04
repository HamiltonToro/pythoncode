#TALLER 6 PYTHON
#AUTOR: Hamilton Toro
#FECHA: 10/11/2023
#Este es el 6to taller trabajando con ciclos iterativos con la sentencia WHILE
from datetime import date
hoy = date.today()     #FECHA ACTUAL
print("En el día de hoy: ", hoy, "trabajermos con ciclos iterativos con la sentencia WHILE")
print()
num1 = int(input("Digite un número: "))
print("***Ciclo controlado por contador***")
i=1
while i<=num1:
        print(i,"",end="")
        i+=1
print()        
print("Fin del ciclo")
print()
print("***Ciclo controlado por evento***")
i=1
numero1=8
numero2=int(input("Adivine un número de 1 a 20 (tiene 5 intentos): "))
while numero2 != numero1:
        if i<=5:
                print("Intento No. ",i)        
                i += 1
                numero2=int(input("Adivine un número de 1 a 20: "))
                continue
        else:
                i=0
if i == 0:
        print("Fallaste")
else:        
        print("Acertaste en el intento No. ",i)
print()
print("Fin del ciclo")
print()
print("***Ciclo abortado con la sentencia break***")
persona=input("Ingrese el nombre de un amigo: ")
persona=persona.upper()
for character in persona:
        print(character)
        if character=="O":
                break
print("Fin del ciclo")
print("Fin del programa")



