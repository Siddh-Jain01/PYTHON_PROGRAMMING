
n = int(input("Enter a number: "))
temp = n
reverse = 0

while temp != 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10

if n == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
