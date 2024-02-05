#print All Fibonacci Numners:

n = int(input("Enter How many Fibonaccci you want to print: "))

def fibonacci(n):
    if n < 0:
        print("Incaract Input")
        
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(n+1))
