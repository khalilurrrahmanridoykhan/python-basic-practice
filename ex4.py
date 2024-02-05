n = int(input("Positive Ineger: "))

sum = 0; i = 1; 

for result in range(1,n+1,1):
    sum = sum + i * i
    i = i +1


print(sum)
