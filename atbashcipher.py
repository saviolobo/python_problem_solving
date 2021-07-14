#in this cipher, in A to Z the first alphabet A becomes Z and B becomes Y and C becomes X and so on...
s=input("Enter the secret message: ")

#removing the spaces if present form the message
w=s.replace(" ", "")

#Check for only alphabets to be present
bool=w.isalpha()

if bool:
    #initializing empty list
    l=[]
    n=w.lower()
    
    for i in w:
        x=ord(i)-97
        #encryption function for atbash cipher
        e=-(x+1)%26   
        y=e+97
        c=chr(y)
        print(c,end="")
else:
    print("Please enter only letters")

    






