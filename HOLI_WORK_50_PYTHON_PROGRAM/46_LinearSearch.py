# 50_Linear_Search.py

arr = list(map(int, input("Enter array elements: ").split()))
key = int(input("Enter key to search: "))
found = False

for num in arr:
    if num == key:
        found = True
        break

print("Name: Siddh jain")
if found:
    print("Element Found")
else:
    print("Element Not Found")
print("Name: Siddh jain")