n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))


print("Array elements are:", *arr)
