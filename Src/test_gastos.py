from gastos import *

def test_lee_gastos(datos):
    print("EJERCICIO 1")
    print("Número de registros leídos:", len(datos))
    print("Primer registro:", datos[0])
    print()

def test_pagadores_y_conceptos(datos):
    print("EJERCICIO 2")
    print("Pagadores:", pagadores_y_conceptos(datos)[0])
    print("Conceptos", pagadores_y_conceptos(datos)[1])
    print()

def test_total_importe(datos):
    print("EJERCICIO 3")
    print("La cantidad total gastada entre el 5 y el 8 de abril de 2019 fue:",\
        total_importe(datos, parsea_fecha("05/04/2019"), parsea_fecha("08/04/2019")))
    print("La cantidad total gastada fue:", total_importe(datos, None, None))
    print()
    
def test_conceptos_menos_gastos(datos):
    print("EJERCICIO 4")
    print("Los conceptos con menos gastos registrados son:", conceptos_menos_gastos(datos))
    print()

def test_pagadores_mayor_importe_medio(datos):
    print("EJERCICIO 5")
    print("Los tres pagadores con un mayor importe medio en sus gastos son: ")
    print(pagadores_mayor_importe_medio(gastos, 3))
    print()





if __name__ == "__main__":
    gastos=lee_gastos("data/gastos.csv")
    test_lee_gastos(gastos)
    test_pagadores_y_conceptos(gastos)
    test_total_importe(gastos)
    test_conceptos_menos_gastos(gastos)
    test_pagadores_mayor_importe_medio(gastos)
    