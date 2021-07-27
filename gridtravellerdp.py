#grid traveller using recursion
#In 2d grid (m,n) where m is rows and n is cols
#find the no. of ways we can reach from source to dest.
#the only moves allowed are down and right

#here we will create a dictionary only if values need to be memoized
def grid(m,n,d={}):
    if m>=0 and n>=0:
        key=m,n
        if key in d:
            return d[key]
        if m==0 or n==0:
            return 0
        elif m==1 and n==1:
            return 1
        else:
            d[key]=grid(m-1,n,d) + grid(m,n-1,d)
            return d[key]
    else:
        print("Negative no. of rows or cols")


m=int(input("Enter the number of rows: "))
n=int(input("Enter the number of cols: "))

result=grid(m,n)

print("The number of ways are: ",result)
