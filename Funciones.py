from ast import Num
import json

def todas_las_armas(datos):
    lista=[]
    for arma in datos:
        armas=arma.get("name")
        lista.append(armas)
    return lista

def contar_las_armas(datos):
    contador=0
    for arma in datos:
        contador=contador+1
    return contador

def arma_por_d(datos):
    lista=[]
    for arma in datos:
        armas=arma.get("name")
        lista.append(armas)
    return lista

def arma_damage(datos,num):
    lista=[]
    for arma in datos:
        armas=arma.get("name"),arma.get("atk").get("physical")
        if arma.get("atk").get("physical")== num:
            lista.append(armas)
    return lista

def arma_magic(datos,num):
    lista=[]
    for arma in datos:
        armas=arma.get("name"),arma.get("atk").get("magic")
        if arma.get("atk").get("magic")== num:
            lista.append(armas)
    return lista