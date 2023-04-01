nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica','FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12,
13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18,
74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64,
87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15,
39, 15, 74, 33, 57, 10]
nombres = nombres.split(",")
def notasSinRepetir(notas_1, notas_2):
    notas_3={x for x in notas_1 or notas_2}
    return notas_3
    
def promEstudiantes(nombres, notas_1, notas_2):
    prom ={}
    for i,n in zip(range(len(notas_2)),nombres):
       prom[n]=(notas_1[i] + notas_2[i]) /2
    return(prom)

def promGeneral (dicc):
    return sum(dicc.values()) / len(dicc)

def promMasBajo (diccGeneral):
    return min (diccGeneral,key = diccGeneral.get)

def promMasAlto (diccGeneral):
    return max(diccGeneral,key = diccGeneral.get)

print(notasSinRepetir(notas_1, notas_2))
dicc = (promEstudiantes(nombres, notas_1, notas_2))
print("el promedio de cada estudiante es"," ", dicc)
print("el promedio general del curso es"," ", (promGeneral(dicc)))
print("el alumno con promedio mas alto es"," ", promMasAlto(dicc))
print("el alumno con promedio mas bajo es"," ", promMasBajo(dicc))