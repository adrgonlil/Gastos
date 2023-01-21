from collections import Counter, namedtuple, defaultdict
from datetime import datetime, date
import csv

Gasto=namedtuple("Gasto","Num_Gasto, Pagador, Concepto, Destinatario, Importe, Fecha ")

def parsea_fecha(cadena):
    return datetime.strptime(cadena, "%d/%m/%Y").date()

def lee_gastos(fichero):
    res=[]
    with open(fichero, encoding="utf-8") as f:
        lector=csv.reader(f)
        next(lector)
        for Num_Gasto, Pagador, Concepto, Destinatario, Importe, Fecha in lector:
            Num_Gasto=int(Num_Gasto)
            Importe=float(Importe)
            Fecha=parsea_fecha(Fecha)
            res.append(Gasto(Num_Gasto, Pagador, Concepto, Destinatario, Importe, Fecha))
    return res

def pagadores_y_conceptos(gastos):
    pagadores=set()
    conceptos=set()
    for g in gastos:
        pagadores.add(g.Pagador)
        conceptos.add(g.Concepto)
    pagadores=sorted(pagadores)
    conceptos=sorted(conceptos)
    return (pagadores, conceptos)

def en_fecha(gasto, f1, f2):
    res = False
    if f1 is None and f2 is None:
        res=True
    elif f1 != None and f2 == None:
        res= gasto.Fecha>=f1
    elif f2 != None and f1 == None:
        res= gasto.Fecha<=f2
    else:
        res=f1<=gasto.Fecha<=f2
    return res

def total_importe(gastos, f_inicial, f_final):
    gasto_final=0
    for g in gastos:
        if en_fecha(g, f_inicial, f_final):
            gasto_final+=g.Importe
    return gasto_final

def  conceptos_menos_gastos(gastos):
    total_por_gastos=Counter(g.Concepto for g in gastos)
    minimo= min(total_por_gastos.values())
    return [concepto for concepto, frecuencia in total_por_gastos.items() if frecuencia == minimo]

def pagadores_mayor_importe_medio(gastos, n):
    dicc=defaultdict(list)
    for g in gastos:
        dicc[g.Pagador].append(g.Importe)
    for pagador, importe in dicc.items():
        dicc[pagador]=sum(importe)/len(importe)
    return sorted(dicc.items(), reverse=True, key=lambda x:x[1])[:n]
    
def numero_pagadores(gastos):
    pagadores=set(g.Pagador for g in gastos)
    lista=list(pagadores)
    return len(lista)
