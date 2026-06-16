n = int(input("Enter a number: "))
sum = 0
temp = n

while temp != 0:
    sum += temp % 10
    temp //= 10


print("Sum of digits =", sum)
