def provjera(br):
    flag=False
    if br<=1:
        flag=True
        
    elif br>1:
        for i in range(2, br):
            if(br%i==0):
                flag=True
                break
            
    if flag:
        print('Nije prost')
    else:
        print('Prost')


n=int(input('Unesi broj:'))
provjera(n)
