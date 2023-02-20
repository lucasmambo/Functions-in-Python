#python program to calculate compound interest using function A=(pow((1+r/100),t))
def compound_Interest(p,r,t):
    ci = p*(pow((1+r/100),t))
    print("Compound Interest = ",ci)
p = float(input("Enter the principal amount ="))
t = float(input("Enter the number of years ="))
r = float(input("Enter the rate of interest ="))
compound_Interest(p,r,t)