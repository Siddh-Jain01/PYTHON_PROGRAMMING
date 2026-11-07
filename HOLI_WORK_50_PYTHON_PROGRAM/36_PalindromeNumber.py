# 36_Palindrome_Number.py

n = int(input("Enter a number: "))
temp = n
reverse = 0

while temp != 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10

print("Name: Siddh jain")
if n == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
print("Name: Shubham Kumar")