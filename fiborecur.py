#print nth number of fibonacii sequence using recursion

def fib(n):
    if(n>0):
        if(n<=2):
            return 1
        else:
            return fib(n-1)+fib(n-2)
    else:
        print("Pl. enter a positive number")
    
n=int(input("Enter the number: "))

result=fib(n)

print("The result is",result)
