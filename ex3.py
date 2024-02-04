import math

p = int(input("Enter Principle amount"))
r = float(input("Enter Interest Rate"))
t = float(input("Enter Time"))


def compound_interest_2021_1_60_097( p1,  r1,  t1):
    a = p1 * math.pow((1 + r1/100),t1)
    # return a
    print("Compound Interest Yearly:",a)


compound_interest_2021_1_60_097(p,r,t)


