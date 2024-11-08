#Ejemplo con Diccionario
from xml.dom.minidom import ProcessingInstruction

diccionario ={} # Diccionario vacio
puertos={
    22:"SSH",
    34:"TELNET",
    80:"HTTP",
    3306:"MYSQL",
    1526:"ORACLE"
}
print(puertos[22])
puertos1 ={
    22:"SSH",
    80:"HTTP"
}
puertos2={
    53:"DNS",
    443:"Https"
}
print(puertos1)
puertos1.update(puertos2) #Actualiza el dicionario
print(puertos1)

#eliminar elmentos del diccionario
calificaciones ={
    "Alumno1":5,
    "Alumno2":4,
    "Alumno3":3,
    "Alumno4":2
}
print(calificaciones)
del calificaciones["Alumno3"]
print(calificaciones)

#Iterar en un  diccioanario
dicPuerto ={
    22:"SSH",
    34:"TELNET",
    80:"HTTP"
}

for x,y in dicPuerto.items():
    print(x,"->",y)