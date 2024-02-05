firstlist = [10,20,11,30,40]
seceondlist = [50,60,61,70,80]
resultlist = firstlist + seceondlist
firstlist1 = []
# print(resultlist)

for i in range(0,len(firstlist)):
    if firstlist[i]%2==0:
        firstlist1 = firstlist1.append(firstlist[i])

print(firstlist1)
# for i in range(0,len(firstlist)):
#     if firstlist[i]%2 == 0:
#         resultlist = 

