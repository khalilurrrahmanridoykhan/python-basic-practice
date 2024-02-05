mystr = input("Enter A string: ")

evenstr = []
oddstr = []

for x in range(0,len(mystr)):
    if x % 2 == 0:
        evenstr.append(mystr[x])

print(evenstr)