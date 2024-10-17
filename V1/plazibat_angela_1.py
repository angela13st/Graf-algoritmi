print('Unesi trojku brojeva')
print('Unesi a:')
a=int(input())
print('Unesi b:')
b=int(input())
print('Unesi c:')
c=int(input())


while(a>0 and b>0 and c>0):
    
    p=[a,b,c]
    p.sort()       
    if ( p[0]**2 + p[1]**2==p[2]**2):
        print('Trojka ', p[0] , ',', p[1], ',', p[2], ' je pitagorejska trojka.' )
    else:
        print('Trojka ', p[0] , ',', p[1], ',', p[2], ' nije pitagorejska trojka.' )
    
    print('Unesi a:')    
    a=int(input())
    print('Unesi b:')
    b=int(input())
    print('Unesi c:')
    c=int(input())
