import math

def provjera(br):
    flag=False
    if br<=1:
        flag=True
        
    elif br>1:
        for i in range(2, br):
            if(br%i==0):
                flag=True
                break
    return flag
            
def prostibrojeviurasponu(n,m):
    brprostih=0
    n=math.ceil(n)
    m=math.ceil(m)
    for i in range(n,m):
        if(provjera(i)==False):
            brprostih+=1
    return brprostih

print('Raspon brojeva')
n=float(input('Unesi prvi broj:'))
m=float(input('Unesi drugi broj:'))

print(prostibrojeviurasponu(n, m))
    