habitaciones = ["chica", "grande", "mediana", "medianita", "chiquita"]

num = int(input("Ingrese numero"))
cont = 0

for habitacion in range(len(habitaciones)):
    if (num-1) <= len(habitaciones):
        while num > cont:
            print(habitaciones[cont])
            cont += 1


# ejercicio incompleto
