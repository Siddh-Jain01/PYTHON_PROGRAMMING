# 49_Find_Max_In_Array.py

arr = list(map(int, input("Enter array elements: ").split()))
max_val = arr[0]

for num in arr[1:]:
    if num > max_val:
        max_val = num

print("Name: Siddh jain")
print("Maximum =", max_val)
print("Name: Siddh jain")