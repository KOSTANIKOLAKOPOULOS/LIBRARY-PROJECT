#INSPECTOR LEKAS

lista1=[]
lista=[]
while True:
    x=input("give bar code of the book or STOP")
    if x=="STOP":
        break
    else:
         lista.append(int(x))
var=max(lista)   
for i in range(0,var):
     if i not in lista :
         lista1.append(i)
print(lista1)

