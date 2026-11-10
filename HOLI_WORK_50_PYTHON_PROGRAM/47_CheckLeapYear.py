# 47_Check_Leap_Year.py

year = int(input("Enter year: "))

print("Name: Siddh jain")
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
print("Name: Siddh jain")