
#================= Lista de comprension de continuacion =================================
def ListCont(fcn, list_ori):
    list_res=[fcn(i) for i in list_ori]
    return list_res
#==================== Lista de comprrension con ciclo for ============================
def ListCond(fcn,list_ori):
    list_res=[fcn(i) for i in list_ori if i%2==0]
    return list_res
#==================== Lista de comprension if-else ===============================
def Listifels(fcn, fcn2, list_1,list_2):
    list_res=[fcn(i) if 1%i==2 else fcn2(j) for i,j in zip(list_1,list_2)]
    return list_res
#====================== Pruebas de las funciones =============================================
List_1=[1,2,3,4]
List_2=[5,6,7,8]
def fat(x):
    return x**2

def fot(x):
    return x+2
#   Prueba primera funcion
print(ListCont(fat, List_1))

#   Prueba segunda funcion
print(ListCond(fot,List_2))

#   Prueba tercera funcion
print(Listifels(fat, fot, List_1, List_2))