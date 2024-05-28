# Write a program to find the largest of three numbers.

a = int(input("Enter the value of A "))
b = int(input("Enter the value of B "))
c = int(input("Enter the value of C "))

if a > b and a > c:
    print(f"The A  is grater with the value of {a}")
elif b >c and b > a:
    print(f"The B is grater with the value of {b}")
else:
    print(f"The C is grater with the value of {c}")