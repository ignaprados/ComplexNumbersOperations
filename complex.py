import cmath
import math
import numpy
from fractions import Fraction
import matplotlib.pyplot as plt
print("  ")
print("-----------------------------------------------------------------------------------------------")
print("El comando p calcula la forma trigonometrica, la forma exponencial y las coordenadas polares")
print("Los comandos s, r, m, d... son para suma, resta, multipliacion, division (en ese orden)")
print("El comando graph permite graficar hasta 10 numeros complejos en un mismo eje cartesiano, segun tu eleccion")
print("-----------------------------------------------------------------------------------------------")
print("  ")
# Este input define que operacion quiere realizar el usuario
#print("------------------------------------------------------------")
print("  ")
op = str(input("Ingrese la operacion que desea realizar. s, r, m, d, p, graph. Ingrese -1 para finalizar el programa:"))



# Se arranca el bucle que contiene el programa. Solo sera terminado si el usuario introduce "-1" en input op

while op != "-1":
    
    # Se le solicita al usuario el primer numero complejo luego de seleccionar la operacion a realizar
    
    x = float(input("Ingrese la parte real del numero complejo:"))
    y = float(input("Ingrese la parte imaginaria del numero complejo:"))
    
    z = complex(x,y)

    # Funcion que calcula el modulo del numero complejo        
    
    def modulo(x,y):
        modul = ((x**2)+(y**2))
        modul = str(modul)
        modul = "√" + modul
        return modul
    
    #Funcion que se encarga de hacer los graficos (no tocar)
    
    def complex_plane2(z,axis_type=0):

        
        w=max(numpy.abs(z1))
        fig, ax = plt.subplots()
            
        if axis_type==0: 
            plt.axis("off")
            plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
            plt.text( 0.8*w,-0.15*w, "Re", fontsize=14)
        elif axis_type==1: 
            plt.axis("on")
            plt.grid()
            plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
            plt.text( 0.8*w,-0.15*w, "Re", fontsize=14)
        else:
             # Move left y-axis and bottim x-axis to centre, passing through (0,0)
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')

            # Eliminate upper and right axes
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')

            # Show ticks in the left and lower axes only
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')

            ax.set_xlabel('                                                 Re []')
            ax.set_ylabel('                                                 Im []')

        plt.xlim(-w,w)
        plt.ylim(-w,w)
        plt.arrow(0, -w, 0, 1.9*w, head_width=w/20, head_length=w/20, fc='k', ec='k');
        plt.arrow(-w, 0, 1.9*w, 0, head_width=w/20, head_length=w/20, fc='k', ec='k');
        plt.title("Complex PY")
        for i in range(len(z1)):
            fi_a=numpy.angle(z1[i])
            x=z[i].real -abs(w)/20*numpy.cos(fi_a)
            y=z[i].imag-abs(w)/20*numpy.sin(fi_a)
            plt.arrow(0, 0, x, y, head_width=w/20, head_length=w/20, fc='b', ec='b');
        plt.show()
    
    # Programa a ejecutar dependiendo de la operacion solicitada por el usuario

    if op == "p":
        
        
        
        

        
        print("---------------------------------------------------------")
        print("  ")
        print("")
        print("Tu numero complejo es=",z)
        print("")
        #polar = cmath.polar(z)
        
        print ("El modulo de tu numero complejo es",modulo(x,y))
        
        # Calcula el argumento del complejo en radianes tipo float
        arg = cmath.phase(z)

        # Convierte el argumento de radianes a grados
        grados1 = numpy.degrees(arg)

        # Este if pone el angulo en el cuadrante correcto
        if grados1 < 0:
            grados = grados1 + 360
        else:
            grados = grados1
        
        print("")
        print("Tu argumento en radianes decimales es =", arg)
        print("")
        print("El argumento en grados es",(grados),"º")

        # Imprimiendo segun el grado del argumento

        if grados == 45:
            print("El argumento en radianes es π/4")
            print("Tu numero complejo en notacion exponencial es:",(modulo(x,y)),"e","^","(","π/4","i",")")
        elif grados == 60:
            print("El argumento en radianes es π/3")
            print("Tu numero complejo en notacion exponencial es:",(modulo(x,y)),"e","^","(","π/3","i",")")
        elif grados == 30:
            print("El aargumento en radianes es π/6")
            print("Tu numero complejo en notacion exponencial es:",(modulo(x,y)),"e","^","(","π/6","i",")")
        elif grados == 90:
            print("El argumento en radianes es π/2")
            print("Tu numero complejo en notacion exponencial es:",(modulo(x,y)),"e","^","(","π/2","i",")")
        
        # Si el angulo no coincide con ninguno de los prestablecidos
        # Calcula el argumentos en radianes fraccion y con π
        # Usando la regla de 3 180----π 
        #                         angulo----x="""
        else:
            rad = grados/180
            rad = round(rad, 2)
        
            rad = str(Fraction(rad).limit_denominator())
            print("")
            print("El argumento en radianes con fracciones y π es = ",rad,"π")
            print("")
            print("Tu numero complejo en notacion exponencial es:",(modulo(x,y)),"e","^","(",rad,"i",")")
            print("")
            print("Tu numero complejo en notacion trigonometrica",(modulo(x,y)),"(cos",rad,"+ isen(",rad,"))")
            print("")
        # Pone el complejo en una lista para poder ser graficado
        z1 = [z]
        # Llama a la funcion para graficar
        complex_plane2(z1,1)
        print("  ")
        print("------------------------------------------------------------")
    elif op == "s":
        # Pide input del segundo numero complejo para hacer la suma
        x2 = int(input("Ingrese la parte real del numero complejo:"))
        y2 = int(input("Ingrese la parte imaginaria del numero complejo:"))
        z2 = complex(x2,y2)
        sum = z + z2
        print("La suma pedida es",sum)
        print("  ")
        print("------------------------------------------------------------")
        text = ("La suma de",z,z2,"=",sum)

        
        z1 = [z,z2,sum]
        complex_plane2(z1,1)

    elif op == "r":
        x2 = int(input("Ingrese la parte real del numero complejo:"))
        y2 = int(input("Ingrese la parte imaginaria del numero complejo:"))
        z2 = complex(x2,y2)
        res = z - z2
        
        print("La resta pedida es",res)
        print("  ")
        print("------------------------------------------------------------")
        z1 = [z,z2,res]
        complex_plane2(z1,1)

    elif op == "m":
         x2 = float(input("Ingrese la parte real del numero complejo:"))
         y2 = float(input("Ingrese la parte imaginaria del numero complejo:"))
         z2 = complex(x2,y2)
         mult = z * z2
         print("La multplicacion pedida es:",mult)
         print("  ")
         print("------------------------------------------------------------")
         z1 = [z,z2,mult]
         complex_plane2(z1,1)

    elif op == "d":
         x2 = float(input("Ingrese la parte real del numero complejo:"))
         y2 = float(input("Ingrese la parte imaginaria del numero complejo:"))
         z2 = complex(x2,y2)
         div = z/z2
         print("La division pedida es=",div)
         print("  ")
         print("------------------------------------------------------------")
         z1 = [z,z2,div]
         complex_plane2(z1,1)

    # La seccion graph se encarga de graficar hasta 10 numeros complejos. Segun el usuario lo indique.
    elif op == "graph":
        cant = int(input("Cuantos numeros complejos mas deseas graficar? Dispible entre 1 y 9"))

        if cant == 1:
            x2 = int(input("Ingrese la parte real del segundo numero complejo:"))
            y2 = int(input("Ingrese la parte imaginaria del segundo numero complejo:"))
            z2 = complex(x2,y2)
            z1 = [z,z2]
            complex_plane2(z1,1)
        elif cant == 2:
            x2 = int(input("Ingrese la parte real del segundo numero complejo:"))
            y2 = int(input("Ingrese la parte imaginaria del segundo numero complejo:"))
            x3 = int(input("Ingrese la parte real del tercer numero complejo:"))
            y3 = int(input("Ingrese la parte imaginaria del tercer numero complejo:"))
            z2 = complex(x2,y2)
            z3 = complex(x3,y3)
            z1 = [z,z2,z3]
            complex_plane2(z1,1)
        elif cant == 3:
            x2 = int(input("Ingrese la parte real del segundo numero complejo:"))
            y2 = int(input("Ingrese la parte imaginaria del segundo numero complejo:"))
            x3 = int(input("Ingrese la parte real del tercer numero complejo:"))
            y3 = int(input("Ingrese la parte imaginaria del tercer numero complejo:"))
            x4 = int(input("Ingrese la parte real del cuarto numero complejo:"))
            y4 = int(input("Ingrese la parte imaginaria del cuarto numero complejo:"))
            z2 = complex(x2,y2)
            z3 = complex(x3,y3)
            z4 = complex(x4,x4)
            z1 = [z,z2,z3,z4]
            complex_plane2(z1,1)

        elif cant == 4:
            x2 = int(input("Ingrese la parte real del segundo numero complejo:"))
            y2 = int(input("Ingrese la parte imaginaria del segundo numero complejo:"))
            x3 = int(input("Ingrese la parte real del tercer numero complejo:"))
            y3 = int(input("Ingrese la parte imaginaria del tercer numero complejo:"))
            x4 = int(input("Ingrese la parte real del cuarto numero complejo:"))
            y4 = int(input("Ingrese la parte imaginaria del cuarto numero complejo:"))
            x5 = int(input("Ingrese la parte real del quinto numero complejo:"))
            y5 = int(input("Ingrese la parte imaginaria del quinto numero complejo:"))
            z2 = complex(x2,y2)
            z3 = complex(x3,y3)
            z4 = complex(x4,x4)
            z5 = complex(x5,y5)
            z1 = [z,z2,z3,z4,z5]
            complex_plane2(z1,1)

        elif cant == 5:
            x2 = int(input("Ingrese la parte real del segundo numero complejo:"))
            y2 = int(input("Ingrese la parte imaginaria del segundo numero complejo:"))
            x3 = int(input("Ingrese la parte real del tercer numero complejo:"))
            y3 = int(input("Ingrese la parte imaginaria del tercer numero complejo:"))
            x4 = int(input("Ingrese la parte real del cuarto numero complejo:"))
            y4 = int(input("Ingrese la parte imaginaria del cuarto numero complejo:"))
            x5 = int(input("Ingrese la parte real del quinto numero complejo:"))
            y5 = int(input("Ingrese la parte imaginaria del quinto numero complejo:"))
            x6 = int(input("Ingrese la parte real del sexto numero complejo:"))
            y6 = int(input("Ingrese la parte imaginaria del sexto numero complejo:"))
            z2 = complex(x2,y2)
            z3 = complex(x3,y3)
            z4 = complex(x4,x4)
            z5 = complex(x5,y5)
            z6 = complex(x6,y6)
            z1 = [z,z2,z3,z4,z5,z6]
            complex_plane2(z1,1)

        elif cant == 6:
            x2 = int(input("Ingrese la parte real del segundo numero complejo:"))
            y2 = int(input("Ingrese la parte imaginaria del segundo numero complejo:"))
            x3 = int(input("Ingrese la parte real del tercer numero complejo:"))
            y3 = int(input("Ingrese la parte imaginaria del tercer numero complejo:"))
            x4 = int(input("Ingrese la parte real del cuarto numero complejo:"))
            y4 = int(input("Ingrese la parte imaginaria del cuarto numero complejo:"))
            x5 = int(input("Ingrese la parte real del quinto numero complejo:"))
            y5 = int(input("Ingrese la parte imaginaria del quinto numero complejo:"))
            x6 = int(input("Ingrese la parte real del sexto numero complejo:"))
            y6 = int(input("Ingrese la parte imaginaria del sexto numero complejo:"))
            x7 = int(input("Ingrese la parte real del septimo numero complejo:"))
            y7 = int(input("Ingrese la parte imaginaria del septimo numero complejo:"))
            z2 = complex(x2,y2)
            z3 = complex(x3,y3)
            z4 = complex(x4,x4)
            z5 = complex(x5,y5)
            z6 = complex(x6,y6)
            z7 = complex(x7,y7)
            z1 = [z,z2,z3,z4,z5,z6,z7]
            complex_plane2(z1,1)
        elif cant == 7:
            x2 = int(input("Ingrese la parte real del segundo numero complejo:"))
            y2 = int(input("Ingrese la parte imaginaria del segundo numero complejo:"))
            x3 = int(input("Ingrese la parte real del tercer numero complejo:"))
            y3 = int(input("Ingrese la parte imaginaria del tercer numero complejo:"))
            x4 = int(input("Ingrese la parte real del cuarto numero complejo:"))
            y4 = int(input("Ingrese la parte imaginaria del cuarto numero complejo:"))
            x5 = int(input("Ingrese la parte real del quinto numero complejo:"))
            y5 = int(input("Ingrese la parte imaginaria del quinto numero complejo:"))
            x6 = int(input("Ingrese la parte real del sexto numero complejo:"))
            y6 = int(input("Ingrese la parte imaginaria del sexto numero complejo:"))
            x7 = int(input("Ingrese la parte real del septimo numero complejo:"))
            y7 = int(input("Ingrese la parte imaginaria del septimo numero complejo:"))
            x8 = int(input("Ingrese la parte real del octavo numero complejo:"))
            y8 = int(input("Ingrese la parte imaginaria del octavo numero complejo:"))
            z2 = complex(x2,y2)
            z3 = complex(x3,y3)
            z4 = complex(x4,x4)
            z5 = complex(x5,y5)
            z6 = complex(x6,y6)
            z7 = complex(x7,y7)
            z8 = complex(x8,y8)
            z1 = [z,z2,z3,z4,z5,z6,z7,z8]
            complex_plane2(z1,1)
        elif cant == 8:
            x2 = int(input("Ingrese la parte real del segundo numero complejo:"))
            y2 = int(input("Ingrese la parte imaginaria del segundo numero complejo:"))
            x3 = int(input("Ingrese la parte real del tercer numero complejo:"))
            y3 = int(input("Ingrese la parte imaginaria del tercer numero complejo:"))
            x4 = int(input("Ingrese la parte real del cuarto numero complejo:"))
            y4 = int(input("Ingrese la parte imaginaria del cuarto numero complejo:"))
            x5 = int(input("Ingrese la parte real del quinto numero complejo:"))
            y5 = int(input("Ingrese la parte imaginaria del quinto numero complejo:"))
            x6 = int(input("Ingrese la parte real del sexto numero complejo:"))
            y6 = int(input("Ingrese la parte imaginaria del sexto numero complejo:"))
            x7 = int(input("Ingrese la parte real del septimo numero complejo:"))
            y7 = int(input("Ingrese la parte imaginaria del septimo numero complejo:"))
            x8 = int(input("Ingrese la parte real del octavo numero complejo:"))
            y8 = int(input("Ingrese la parte imaginaria del octavo numero complejo:"))
            x9 = int(input("Ingrese la parte real del noveno numero complejo:"))
            y9 = int(input("Ingrese la parte imaginaria del noveno numero complejo:"))
            z2 = complex(x2,y2)
            z3 = complex(x3,y3)
            z4 = complex(x4,x4)
            z5 = complex(x5,y5)
            z6 = complex(x6,y6)
            z7 = complex(x7,y7)
            z8 = complex(x8,y8)
            z9 = complex(x9,y9)
            z1 = [z,z2,z3,z4,z5,z6,z7,z8,z9]
            complex_plane2(z1,1)
        elif cant == 9:
            x2 = int(input("Ingrese la parte real del segundo numero complejo:"))
            y2 = int(input("Ingrese la parte imaginaria del segundo numero complejo:"))
            x3 = int(input("Ingrese la parte real del tercer numero complejo:"))
            y3 = int(input("Ingrese la parte imaginaria del tercer numero complejo:"))
            x4 = int(input("Ingrese la parte real del cuarto numero complejo:"))
            y4 = int(input("Ingrese la parte imaginaria del cuarto numero complejo:"))
            x5 = int(input("Ingrese la parte real del quinto numero complejo:"))
            y5 = int(input("Ingrese la parte imaginaria del quinto numero complejo:"))
            x6 = int(input("Ingrese la parte real del sexto numero complejo:"))
            y6 = int(input("Ingrese la parte imaginaria del sexto numero complejo:"))
            x7 = int(input("Ingrese la parte real del septimo numero complejo:"))
            y7 = int(input("Ingrese la parte imaginaria del septimo numero complejo:"))
            x8 = int(input("Ingrese la parte real del octavo numero complejo:"))
            y8 = int(input("Ingrese la parte imaginaria del octavo numero complejo:"))
            x9 = int(input("Ingrese la parte real del noveno numero complejo:"))
            y9 = int(input("Ingrese la parte imaginaria del noveno numero complejo:"))
            x10 = int(input("Ingrese la parte real del decimo numero complejo:"))
            y10 = int(input("Ingrese la parte imaginaria del decimo numero complejo:"))
            z2 = complex(x2,y2)
            z3 = complex(x3,y3)
            z4 = complex(x4,x4)
            z5 = complex(x5,y5)
            z6 = complex(x6,y6)
            z7 = complex(x7,y7)
            z8 = complex(x8,y8)
            z9 = complex(x9,y9)
            z10 = complex(x10,y10)
            z1 = [z,z2,z3,z4,z5,z6,z7,z8,z9,z10]
            complex_plane2(z1,1)

    #elif op == raiz:

        #n = int(input("Ingrese el indice de la raiz"))

        #raiz = x^(1/n)

        #calc = 
        


       







    op = str(input("Ingrese la operacion que desea realizar. s, r, m, d, p, graph.- Ingrese -1 para finalizar el programa:"))
    print("  ")
    print("------------------------------------------------------------")

