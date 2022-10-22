cont = 0
LIMITADOR = 2
lista = []
objecto = {} 
while(cont < LIMITADOR):
   objecto ['nombre'] = input("digitar Nombre: ")  
   objecto ['color'] = input("digitar Color: ")
   objecto ['precio'] = input("digitar Precio: ")
   cont += 1
   lista.append(objecto)

lista.reverse()
print(f"{lista}")