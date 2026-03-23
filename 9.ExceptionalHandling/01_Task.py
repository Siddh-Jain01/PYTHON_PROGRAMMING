try :
     a= int(input("enter a number:"))
     b= int(input("enter b number:"))
     print(a/b)
except ZeroDivisionError:

    print("you cannot Divide by zero:")
except ValueError:
     print("invalid input plz enter a valid number :")
     