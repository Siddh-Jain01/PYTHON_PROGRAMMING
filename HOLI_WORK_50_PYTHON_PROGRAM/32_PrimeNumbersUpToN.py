# 32_Prime_Numbers_Up_To_N.py

n = int(input("Enter a number: "))

print("Name: Siddh jain")
print("Prime numbers up to", n, ":")

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
print("\nName: Siddh jain")