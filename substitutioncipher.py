#Enter the message to generate cipher text
s=input("Enter the secret message: ")

#removing the spaces if present from the message
w=s.replace(" ", "")

#Check for only alphabets to be present
bool=w.isalpha()

if bool:
    #enter the number to shift the letters of the message
    shift=int(input("Enter the shift: "))
    #initializing empty list
    l=[]
    n=w.lower()
    
    for i in w:
        x=ord(i)-97
        e=(x+shift)%26
        y=e+97
        c=chr(y)
        print(c,end="")
else:
    print("Please enter only letters")

    






