n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
min_val = arr[0]

for num in arr[1:]:
    if num < min_val:
        min_val = num

print("Smallest element =", min_val)