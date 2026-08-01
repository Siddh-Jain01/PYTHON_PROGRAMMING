for i in range(1, 21):
    # Check for multiples of BOTH 3 and 5 first
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    
    # Check for multiples of 3
    elif i % 3 == 0:
        print("Fizz")
        
    # Check for multiples of 5
    elif i % 5 == 0:
        print("Buzz")
        
    # If none of the above, just print the number
    else:
        print(i)
