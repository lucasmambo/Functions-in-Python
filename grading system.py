#python program for grading system using function
def grade(a,b,c):
    avg = (a+b+c)/3
    print("Average = ", avg)
    if avg >=70 and avg<=100:
        print("Grade = A")
    elif avg>=60 and avg<=69:
        print("Grade = B")
    elif avg >= 50 and avg <= 59:
        print("Grade = C")
    elif avg >= 40 and avg <=49:
        print("Grade = D")
    elif avg >=0 and avg <=39:
        print("Grade = D")
    else:
        print("Try Again!")
a = int(input("Enter Unit a Marks out of 100 ="))
b = int(input("Enter Unit b Marks out of 100 ="))
c = int(input("Enter Unit c Marks out of 100 ="))
grade(a,b,c)