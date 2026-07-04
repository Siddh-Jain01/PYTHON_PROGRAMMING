n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
max_val = arr[0]

for num in arr[1:]:
    if num > max_val:
        max_val = num

print("Largest element =", max_val)