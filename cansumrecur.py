#given sum and array of elements,return true if the elements of array on adding give the sum or return false
#elements in the array can be used as many times as needed to form sum. Sum can be zero or positive integers.Numbers in array can be zero or positive integers.
#using recursion as brute force

import array as arr
a=arr.array('i',[])

def cansum(tsum,a):
    if (tsum==0):
        return True
    if (tsum<0):
        return False
    for num in a:
        if (num>0):
            rem=tsum-num
            if cansum(rem,a)==True:
                return True
        else:
            return "Numbers in array are either 0 or negative"
    return False

#in order to take input from user for target sum and array of numbers        
tsum=int(input("Enter the target sum: "))
n=int(input("Enter the number of elemets for the array: "))
for i in range(0,n):
    x=int(input("Enter the number: "))
    a.append(x)

result=cansum(tsum,a)

print("Targets sum achieved?",result)
