# 17_Sum_of_Digits.py

n = int(input("Enter a number: "))
sum = 0
temp = n

while temp != 0:
    sum += temp % 10
    temp //= 10

print("Name: Siddh jain")
print("Sum of digits =", sum)
print("Name: Siddh jain")