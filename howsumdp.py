#given sum and array of elements return an array having combination that gives target sum or return null
#if multiple combinations return single one
#using dynamic programming

import array as arr
a=arr.array('i',[])
b=arr.array('i',[])

def howsum(tsum,a,dict={}):
    if (tsum in dict):
        return dict[tsum]
    if (tsum==0):
        return []
    if (tsum<0):
        return None
    for num in a:
            rem=tsum-num
            b=howsum(rem,a,dict)
            if (b!=None):   
                dict[tsum]=b.append(num)
                return dict[tsum]
    dict[tsum]=None
    return dict[tsum]
              
            
#in order to take input as target sum and array of numbers        
tsum=int(input("Enter the target sum: "))
n=int(input("Enter the number of elemets for the array: "))
for i in range(0,n):
    x=int(input("Enter the number: "))
    a.append(x)

result=howsum(tsum,a)

print("The combination that gives target sum: ",result)

