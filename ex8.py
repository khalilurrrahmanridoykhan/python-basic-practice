numarray = [10,20,30,40,51]
sum = 0
# print(len(numarray))

for x in range(0,len(numarray)):
    if(numarray[x]%2 == 0):
        sum = sum + numarray[x]   
        

print(sum)