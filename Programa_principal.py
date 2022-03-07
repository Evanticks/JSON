import json
from Funciones import *
with open("DarkSoulsWeapons.json") as fichero:
    datos=json.load(fichero)

print ('''
1.  Listar todas las armas.
2.  Contar las armas que hay.
3.  Mostrar armas que empiecen por D.
4.  Mostrar el número de ataque y que muestre el nombre de las armas relacionadas.
5.  Muestra el daño mágico de las armas.
0.  Salir.''')

opcion=int(input("Selecciona una opción: "))

while opcion !=0 :
    if opcion == 1:
        lista=todas_las_armas(datos)
        for i in lista:
            print (i)
    if opcion == 2:
        lista=contar_las_armas(datos)
        print (lista)
    if opcion == 3:
        lista=arma_por_d(datos)
        check="D"
        res = [idx for idx in lista if idx[0].lower() == check.lower()]
        for i in res:
            print (f"\n-nombre: {i}")
    if opcion == 4:
        num=int(input("Dime el número de ataque"))
        lista=arma_damage(datos,num)
        for i in lista:
            print (f"\n-nombre: {i[0]}\n -ataque físico: {i[1]}")
    if opcion == 5:
        num=int(input("Dime el número de ataque mágico"))
        lista=arma_damage(datos,num)
        for i in lista:
            print (f"\n-nombre: {i[0]}\n -ataque mágico: {i[1]}")
    opcion=int(input("Selecciona una opción: "))
