# 40_Smallest_Of_Three_Numbers.py

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Name: Siddh jain")
if a <= b and a <= c:
    print("Smallest =", a)
elif b <= c:
    print("Smallest =", b)
else:
    print("Smallest =", c)
print("Name: Siddh jain")