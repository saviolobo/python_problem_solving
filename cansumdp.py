#given sum and array of elements,return true if the elements of array on adding give the sum or return false
#elements in the array can be used as many times as needed to form sum
#Sum can be zero or positive integers.Numbers in array can be zero or positive integers.
#using dynamic programming

import array as arr
a=arr.array('i',[])

#dictionary is used for memoization
def cansum(tsum,a,dict={}):
    if (tsum in dict):
        return dict[tsum]
    if (tsum==0):
        dict[tsum]=True
        return dict[tsum]
    if (tsum<0):
        dict[tsum]=False
        return dict[tsum]
    for num in a:
        if (num>0):
            rem=tsum-num
            dict[tsum]=cansum(rem,a,dict)
            if dict[tsum]==True:
                return dict[tsum]
        else:
            return "Numbers in array are either 0 or negative"
    dict[tsum]=False
    return False

#in order to take input from user for target sum and array of numbers        
tsum=int(input("Enter the target sum: "))
n=int(input("Enter the number of elemets for the array: "))
for i in range(0,n):
    x=int(input("Enter the number: "))
    a.append(x)

result=cansum(tsum,a)

print("Target sum achieved?",result)
