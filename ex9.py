numarray = [300,10,20,30,40,51]
max = numarray[0]
min = numarray[0]

def max_num(numarray, max):
    for x in numarray:
        if(x>max):
            max = x
    return max
def min_num(numarray, min):
    for x in numarray:
        if(x<min):
            min = x
    return min    
    

print(max_num(numarray,max))
print(min_num(numarray,min))