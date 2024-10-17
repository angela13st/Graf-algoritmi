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

def nprostibroj(n):
    prostibroj=0
    brojac=0
    i=2
    while brojac<n:
        if provjera(i)==False:
            prostibroj=i
            brojac+=1
            #print(prostibroj)
        i+=1
    return prostibroj

n=int(input('Unesi broj:'))
print(n, '. prosti broj:', nprostibroj(n))