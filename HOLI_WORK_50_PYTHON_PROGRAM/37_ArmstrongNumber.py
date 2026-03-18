# 37_Armstrong_Number.py

n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
sum = 0

while temp != 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

print("Name: Siddh jain")
if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
print("Name: Siddh jain")