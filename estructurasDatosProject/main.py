#ejemplo con tuplas
from pickle import PROTO

tupla1 =()  #tupla vacia
print(tupla1)
#------------------------
tupla2=("apple",2018,"samsung ",4.9," t ", True)
print(tupla2)
print(tupla2[1])

print(tupla2[3])

#-------------------opercion con tuplas
tupla3= ("a ","b ","C ","D")
tupla4 =(1,2,3,4)
#concatenar
tupla5 = tupla3+tupla4
print(tupla5)
#-----------repetirlas
tupla6 =tupla3*3
print(tupla6)
#----------Tupla Enlazada
tupla7= (0,1,2,3)
tupla8=("A","B","C")
tupla9=(tupla7,tupla8)
print(tupla9)
print(tupla9[1])

print(tupla9[1][1])

#-----------COmparar
tupla10 =("Rojas ")
tupla11=(123)
tupla12=("Rosas")
tupla13=("rosas")
print(tupla10 < tupla12)