import numpy as np
while True:

    lista=[]
    valor=float(input("Ingresar valor (100 para finalizar):"))
    while valor!=100:
        lista.append(valor)
        valor=float(input("Ingresar valor (100 para finalizar):"))

    print(np.roots(lista))

