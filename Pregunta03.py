from random import*
def aleatorio():
    p=[]
    n=[]
    for i in range(1,7):
        x=random.randint(1,10)
        p=p+[x]
    print(p)
    for b in p:
        if b not in  n:
            n=n+[b]
    print(n)

a=int(input("digite 6 numeros entre 1 al 10 :"))
v=[]
alea=[]
if a>=1 and a<=10:

    for i in range(1,7):
        x=int(input("digite 6 numeros distintos entre 1 al 10 :"))
        v=v+[x]
    print("numeros salido ",v)  
aleatorio()

    


