# 31_Prime_Number.py

n = int(input("Enter a number: "))
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            is_prime = False
            break

print("Name: Siddh jain")
if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")
print("Name: Siddh jain")