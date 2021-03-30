import numpy as np
import random
#generador de poblacion
def matrices50(x, y, z):
    AM = np.zeros([x, y, z])
    for n in range(0, z):
        for i in range(0, y):
            p = random.randrange(0, y)
            AM[i, p, n] = 1
    return AM
#seleccionador de padres y creacion de hijos
def f(a, b):
    r1 = a
    r2 = b
    for i in range(8):
        if random.random() >= 0.5:
            for j in range(8):
                r1[i, j] = a[i, j]
                r2[i, j] = b[i, j]
        else:
            for j in range(8):
                r1[i, j] = b[i, j]
                r2[i, j] = a[i, j]
    return r1, r2

#mutacion de hijos
def mutacion_matriz(matriz):
    matriznueva=matriz
    matrix_zeros = np.zeros((8, 8))
    fila_1 = random.randrange(0, 8) #Genera aleatoriamente las filas que se van a intercambiar
    fila_2 = random.randrange(0, 8)
    #print(fila_1, fila_2)
    matrix_zeros[fila_1] = matriznueva[fila_1]
    matriznueva[fila_1] = matriznueva[fila_2]
    matriznueva[fila_2] = matrix_zeros[fila_1]
    #print(matriznueva)
    return matriznueva


#funcion de reemplazo
def remplazo(numgen):
    cont_1=0
    cont_2=0
    poblacion = matrices50(8, 8, 50)
    while cont_2<=numgen:
        nuevapob=[]
        while cont_1 <50:
            papa_1 = poblacion[:, :, random.randrange(0, 50)]
            papa_2 = poblacion[:, :, random.randrange(0, 50)]
            h1,h2=f(papa_1,papa_2)
            hm1=mutacion_matriz(h1)
            hm2=mutacion_matriz(h2)
            nuevapob.append(hm1)
            nuevapob.append(hm2)
            cont_1+=2
        cont_2+=1
        memoria=nuevapob
        return memoria#, poblacion
    """ En la cuncion de remplazo, se puede borrar el # y entonces esta tambien imprimira la poblacion original"""

#funcion de aptitud
def aptitudfcn(matriz):
    cont=0
    #Esta parte concierne a las diagonales del tipo \
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            pos_in = matriz[i][(len(matriz) - 2) - j]
            memoria = (len(matriz) - 2) - j
            for m in range(1, len(matriz) ):
                if (i+m) < len(matriz) and (memoria+m) < len(matriz):
                    elem_diag = matriz[i+m][memoria + m]
                    if (pos_in == 1) and (pos_in == elem_diag):
                        cont += 1
    #Esta parte es para las diagonales del tipo /
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            pos_in = matriz[len(matriz)-1-j][len(matriz)-1-i]
            memoria_1=len(matriz)-1-j
            memoria_2=len(matriz) - 1 - i
            for m in range(1,len(matriz)):
                if (memoria_1 + m)<len(matriz) and (memoria_2-m)>= 0:
                    elem_diag=matriz[memoria_1 + m][memoria_2-m]
                    if (pos_in == 1) and (elem_diag == pos_in):
                        cont += 1
    #columnas
    for i in range(0, len(matriz)):
        for j in range (0, len(matriz)):
            pos_in=matriz[i][j]
            for m in range(1, len(matriz)):
                if ((i+m)<len(matriz)):
                    elem_col =matriz[i+m][j]
                    if (pos_in == 1) and pos_in==elem_col:
                        cont += 1
#filas. Se que aqui no necesariamente se hace por que de hecho siempre da cero,
    # pero no esta por demas aumentarla si cambiasemos el criterrio de las

    for i in range(0,len(matriz)):
        for j in range(0, len(matriz)):
            pos_in=matriz[j][i]
            for m in range(1,len(matriz)):
                if (i+m)<len(matriz):
                    elem_fil=matriz[j][i+m]
                    if (pos_in ==1) and pos_in == elem_fil :
                        cont+=1
    numero_ataques=cont

    return numero_ataques

#Algoritmo genetico
def alg_gen(num_gen):
    poblacion_fin=remplazo(num_gen)
    atk_x_ind=[]
    apropiados=[]
    for i in range(0,len(poblacion_fin)):
        indi=poblacion_fin[i]
        atk_x_ind.append(aptitudfcn(indi))
    for i in range(0, len(atk_x_ind)):
        atk=atk_x_ind[i]
        if min(atk_x_ind)==atk:
            apropiados.append(poblacion_fin[i])

    print('El individuo o individuos mas apropiado despues de ', num_gen, 'generaciones y con ',min(atk_x_ind),' ataques es' )
    print(apropiados)



