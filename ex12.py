mystr = input("Enter Your String: ")
mynum = int(input("Enter Your Number: "))
newstr = ''

for y in range(0,len(mystr)):
    if(y>=mynum):
        
        newstr = newstr + mystr[y]
        
print(newstr)