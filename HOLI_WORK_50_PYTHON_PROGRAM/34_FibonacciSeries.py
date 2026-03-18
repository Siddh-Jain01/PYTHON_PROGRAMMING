# 34_Fibonacci_Series.py

n = int(input("Enter number of terms: "))
a, b = 0, 1

print("Name: Siddh jain")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print("\nName: Siddh jain")