# 25_Count_Even_and_Odd_Elements.py

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
even = odd = 0

for num in arr:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Name: Siddh jain")
print("Even =", even)
print("Odd =", odd)
print("Name: Siddh jain")