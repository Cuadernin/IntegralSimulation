from random import * 
from math import * 
from sympy import *
from sympy.abc import x,z 
"""
Calcular cualquier integral definida usando simulacion de Monte Carlo By Cuadernin. 
"""
def func(f,a,b): 
    x=z*(b-a)+a    
    return x 
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MENU <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<") 
print("Opcion 1 ----> Cambia cualquier integral f(x) en [a,b] a una integral de [0,1]") 
print("Opcion 2 ----> Cambia cualquier integral de f(x) en [0,oo) a una integral de [0,1]") 
print("Opcion 3 ----> Cambia cualquier integral de f(x) en (oo,oo) a una integral de [0,oo)") 
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<") 
opc=int(input("\nEscriba la opcion deseada: ")) 
if opc==1: 
    funcion=input("\nEscriba la funcion en terminos de x(ejemplo: x**2+1 ,sqrt(x+2)): ")     
    a=float(input("Escriba el limite inferior de la integral: "))
    b=float(input("Escriba el limite superior de la integral: "))     
    N=1000000 ## change this value for more precision  
    assert b>a,"********EL LIMITE SUPERIOR DEBE SER MAYOR QUE EL LIMITE INFERIOR***********"
    sol=integrate(funcion,(x,a,b))
    if sol==oo or sol==nan:
        print(f"La solucion real es divergente")
    else:
        funci=sympify(funcion).subs(x,func(funcion,a,b)) 
        funci=(b-a)*funci
        suma=0 
        print("======================= La integral se convierte a: ===========================")     
        pprint(pretty(Integral(funci,(z,0,1)),use_unicode=False))     
        print("===============================================================================") 
        f=lambdify(z,funci)
        ###########  Simulation part
        for i in range(N):         
            s=random()          
            suma=suma+f(s) 
        print(f"\nLa aproximacion final es {suma/N}")
        print(f"La solucion real es {sol}")
        print(f"Error porcentual = {(sol-suma/N)/sol}\n")
        ###########
elif opc==2: 
    funcion=input("Escriba la funcion en terminos de x(ejemplo: x**2+1 ,sqrt(x+2) ): ") 
    sol=integrate(funcion,(x,0,oo))
    N=1000000 ## change this value for more precision   
    if sol==oo or sol==nan:
        print(f"La solucion real es divergente")  
    else:  
        funci=sympify(funcion).subs(x,1/z-1)   
        funci=funci/z**2 
        suma=0 
        print("======================= La integral se convierte a: ===========================") 
        pprint(pretty(Integral(funci,(z,0,1)),use_unicode=False)) 
        print("===============================================================================")     
        f=lambdify(z,funci)
        ###########   
        for i in range(N):        
            s=random()          
            suma=suma+f(s)    
        print(f"\nLa aproximacion final es {suma/N}")
        print(f"La solucion real es {sol}")
        print(f"Error porcentual = {(sol-suma/N)/sol}\n")
        ###########  
elif opc==3: 
    funcion=input("Escriba la funcion en terminos de x(ejemplo: x**2+1 ,sqrt(x+2) ): ") 
    N=1000000 ## change this value for more precision
    sol=integrate(funcion,(x,-oo,oo))
    if sol==oo or sol==nan:
        print(f"La solucion real es divergente") 
    else:    
        funci1=sympify(funcion).subs(x,1/z)    
        funci2=sympify(funcion).subs(x,1-1/z)    
        funci1=funci1/z**2     
        funci2=funci2/z**2     
        print("======================= La integral se convierte a: ===========================")     
        pprint(pretty(Integral(funci1,(z,0,1))+Integral(funci2,(z,0,1)),use_unicode=False))     
        print("===============================================================================")     
        suma1,suma2=0,0 
        f1=lambdify(z,funci1)     
        f2=lambdify(z,funci2)  
        ###########     
        for i in range(N): 
            s=random() 
            suma1=suma1+f1(s)          
            suma2=suma2+f2(s)     
            n=suma1+suma2     
        print(f"\nLa aproximacion final es {n/N}")
        print(f"La solucion real es {sol}")
        print(f"Error porcentual = {(sol-n/N)/sol}\n")
        ###########  
else: 
    print("*******NO EXISTE ESA OPCION********") 

