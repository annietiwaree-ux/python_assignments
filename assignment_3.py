def right_triangle(a, b, c):
    if a*a + b*b == c*c:
        print("It is a right-angled triangle")
    else:
        print("It is not a right-angled triangle")

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

right_triangle(a, b, c)
