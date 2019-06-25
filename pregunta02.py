#una historia de usuario es la solucion a un problema(que es lo que desea,para que lo desea y como quieres tal proyeecto)
#por ejemplo una persona quiere que se implemente una aplicacion para
#poder calcular el premedio de su trabajo
#el cual consta de 2 practicas 
a=int(input("Nota practica 1 : "))
b=int(input("Nota practica 2 : "))

if a <0 and b<0:
    print("ingrese una nota valida")
else:
    print("su nota promedio es",(a+b)/2)
