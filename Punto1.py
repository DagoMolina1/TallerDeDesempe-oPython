n = int(input("Digita la cantidad de numeros a ingresar: "))
print(f"la cantidad digita es: {n}")
cont = 0
contMultiplos2 = 0
contMultiplos3 = 0
lista = []
while(cont < n):
   elemento = int(input("digitar elemento a agregar: "))
   lista.append(elemento)
   cont += 1
for e in lista:
    if(e % 2 == 0 and e % 3 == 0 ):
        contMultiplos2 += 1
        contMultiplos3 += 1
        print(f"{e} es multiplo de 2 y de 3")
    elif(e % 2 == 0):
        contMultiplos2 += 1
        print(f"{e} es multiplo de 2")
    elif(e % 3 == 0):
         contMultiplos3 += 1
         print(f"{e} es multiplo de 3")
    else:
        print(f"{e} no es multiplo ni de 2 ni de 3")
   
print(f"los multiplos de dos son {contMultiplos2}")
print(f"los multiplos de tres son {contMultiplos3}")