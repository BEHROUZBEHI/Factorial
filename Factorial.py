num = int(input("Enter num: "))

def facturiel(num):
    a=1
    for i in range (1,num):
        a= a*(i+1)
    return(a)
print(facturiel(num))
