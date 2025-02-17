import numpy as np
#ex1
nomes=input("nomes")
tempos=input("tempos")
pilotos=np.array(nomes.split(", "))
voltas=np.array(tempos.split(", "))
i=0
while (i<5):
    if int(voltas[i])<=0:
        voltas[i]=int(input("..."))
    else:
        i+=1
for i in range(5):
    if int (voltas[i])<int(voltas[pm]):
        pm=i
    if int(voltas[i])>int(voltas[pm]):
        pp=i
diferença=voltas[pp]-int(voltas[pm])
print("primeiro",pilotos[pm])
print("ultimo",pilotos[pp])
print("diferença,diferença")
for i in range(5):
    print(f"{pilotos[i]}:{voltas[i]}")

#ex2
contar=0
email=input("email")
pp=input("palavra passe")
if len(pp)>8:
    contar=contar+1
    if pp not in email:
        contar=contar+1
for i in pp:
    if i>="a" and i<="z":
        contar=contar+1
    break
for l in pp:
    if l>"A" and l<"Z":
        break
for l in pp:
    if l>"0" and l<"9":
        contar=contar+1
        break
