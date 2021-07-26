#print nth number of fibonacii sequence using recursion

def fib(n):
    if(n>0):
        if(n<=2):
            return 1
        else:
            return fib(n-1)+fib(n-2)
    
n=int(input("Enter the number: "))

result=fib(n)

print("The number is",result)
