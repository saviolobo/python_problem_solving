#print nth number of fibonacii sequence using dynamic programming
#declaring a dictionary for memoization
m={}

def fib(n):
    if(n>0):
        if (n in m):
            return m[n]
        if(n<=2):
            return 1
        else:
            m[n]=fib(n-1)+fib(n-2)
            return m[n]
    else:
        print("Pl. enter a positive no.")
    
n=int(input("Enter the number: "))

result=fib(n)

print("The result is",result)
