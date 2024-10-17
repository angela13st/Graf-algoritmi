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

def Goldbach(n):
    if(n%2!=0 or n<=2):
        print('Uneseni broj nije paran ili nije veći od 2')
        return
    for i in range(2,n):
        drugi_pribrojnik=n-i
        if(provjera(i)==False and provjera(drugi_pribrojnik)==False):
            print(n, '=', i ,'+' , drugi_pribrojnik)
            
n=int(input('Unesi broj:'))
Goldbach(n)