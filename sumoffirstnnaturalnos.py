#program to print sum of first n natural numbers upto a range that the user gives as input
#natural numbers are used for counting and make use of positive integes

#Enter range upto which you want to print the sum of first n natural numbers
n=int(input("Enter the number upto:"))

#if-else condition to check if the number is valid positive integer upto which we need to display sum.
if n<=0:
    print("Not a natural number")
else:
    i=1
    sum=0
    while i<=n:
        sum=sum+i
        i=i+1
    print("The sum of first ",n,"natural numbers:",sum)

   
    
