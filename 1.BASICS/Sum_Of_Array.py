n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
sum = 0

for num in arr:
    sum += num
print("Sum =", sum)