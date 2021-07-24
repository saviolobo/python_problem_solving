#sum of first n positive numbers using recursion
def sum(num):
    if num==1:
        return num
    elif(num>1):
        return num + sum(num-1)
    else:
        print("Please enter a positive number")
    
num=int(input("Enter the number of terms:"))

result=sum(num)

print("The sum is: ",result)
