import sys

nota_1= int(sys.argv[1])
nota_2= int(sys.argv[2])

if nota_1 and nota_2 >=7:
    print("Promocionado")

elif nota_1 and nota_2 >= 4:
    print("Aprobado, debe rendir final")
    
elif nota_1 or nota_2 < 4:
    print("Debe recuperar el parcial desaprobado")

elif nota_1 and nota_2 < 4:
    print("Desaprobo ambos parciales, debe recursar")

else:
    print("Debe ingresar 2 notas")
    