#Tipos de variables 

nombre ="Yordy" #str
edad = 18 #int
estatura = 1.78 #float
es_estudiante = True #bool

print (f"Nombre: {nombre }, (tipo: {type(nombre)})")
print (f"Edad: {edad }, (tipo: {type(edad)})")
print (f"Estatura: {estatura }, (tipo: {type(estatura)})")
print (f"Es estudiante: {es_estudiante }, (tipo: {type(es_estudiante)})")



#Entrada de un bar 

nombre=  input ("Ingresar tu nombre: ")
edad = int(input("ingresar tu edad: "))
mayor_de_edad = edad >=18
estatura = float(input("ingresa tu estatura en metros: "))

print(f"\nResumende datos:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"¿es mayor de edad? {mayor_de_edad}")
print(f"Estatura: {estatura:.2f} metros")



