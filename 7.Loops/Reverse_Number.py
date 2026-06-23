n = int(input("Enter a number: "))
reverse = 0
temp = n

while temp != 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10


print("Reversed Number =", reverse)
