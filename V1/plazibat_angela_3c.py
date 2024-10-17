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

def prostisusjedni(n):
    susjedni=[]
    i=2
    while i<=n:
        if (provjera(i)==False):
            sljedbenik=i+2
            prethodnik=i-2
            if(provjera(sljedbenik)==False or provjera(prethodnik)==False):
                susjedni.append(i)
        i+=1
    return susjedni

n=int(input('Unesi broj:'))
print('Susjedni prosti brojevi:', prostisusjedni(n))
