#ejemplo con listas
lista=[]
lista1=[1,"Hola ",4.5, "8"]
print(lista1)
print(lista1[1][2])#elemnto dentro del indice 1

#lista enlazada
lista2 =[1,2,3,4]
lista3 = ["A", "B","C"]
lista4 =[lista2,lista3]
print(lista4[1][2])

lista6=[1,2,3,4]
lista5 = ["A", "B","C"]
lista7 =lista5+lista6
print(lista7)

#---repetir
lista8=[1,2,3,4,5]
lista9=lista8*4
print(lista9)

#comparacion
lista10=["Juan"]
lista11=["juan"]
print(lista10 == lista11)
#determinar si un elemento se emcuentra
lista12= ["cien ","años","de","soledad "]
if "de" in lista12:
    print("si esta en la lista")
else:
    print("no esta en la lista ")
#iterar un lista
lista13 = ["Hola ","Estudiantes","programacion","Fup"]
for palabra in lista13:
    print(palabra, end =",")
