#given sum and array of elements return an array having shortest combination that adds up to target sum
#if tie return single one
#using recursion as brute force

import array as arr
a=arr.array('i',[])
comb=arr.array('i',[])

def bestsum(tsum,a):
    if (tsum==0):
        return []
    if (tsum<0):
        return None
    best=None
    for num in a:
            rem=tsum-num
            comb=bestsum(rem,a)
            if (comb!=None):   
                comb.append(num)
                if (best==None or len(comb)<len(best)):
                    best=list(comb)
                
    return best
              
            
#in order to take input as target sum and array of numbers        
tsum=int(input("Enter the target sum: "))
n=int(input("Enter the number of elemets for the array: "))
for i in range(0,n):
    x=int(input("Enter the number: "))
    a.append(x)

result=bestsum(tsum,a)

print("The combination that gives target sum: ",result)

