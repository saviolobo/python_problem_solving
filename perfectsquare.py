n=int(input("Enter the no.:"))

def ps(n):
    if (n<=0):
        return "It is not a perfect square"              
    else:
        i=1
        while(i<=n):
            p=i*i
            if(n==p):
                return "It is a perfect Square" 
            else:
                i=i+1
    return "It is not a perfect square"

result=ps(n)

print(result)
