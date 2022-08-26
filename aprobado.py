import sys

nota_1= int(sys.argv[1])
nota_2= int(sys.argv[2])

if nota_1 and nota_2 >= 0 and 10:

    if nota_1 and nota_2 >=7:
        print("Promocionado")

    elif nota_1 >= 4 and nota_2 >= 4:
        print("Aprobado, debe rendir final")
        
    elif nota_1 < 4 and nota_2 >=4:
        print("Debe recuperar el primer parcial")

    elif nota_1 >=4 and nota_2 < 4:
        print("Debe recuperar el segundo parcial")

    elif nota_1 <= 3 and nota_2 <= 3:
        print("Desaprobo ambos parciales, debe recursar")

    else:
        print("Debe ingresar 2 notas")

else:
    print("Debe ingresar notas del 0 al 10")