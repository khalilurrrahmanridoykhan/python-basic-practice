n = int(input("Enter The Numner: "))

def prime_find_2021_1_60_097(num):
    if num > 1:
        for x in range(2,int(n/2)+1):
            if n%x == 0:
                print("This is Not A prime Number")
                break
            else:
                print("This is A prime Number")
                break
    else:
        print("This is Not A Prime Number.")
        

prime_find_2021_1_60_097(n)
    