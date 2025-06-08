def check_age(age):
    age = int(age)
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age%2 == 0:
        print(f"{age} is even")
    else:
        print(f"{age} is odd")

except ValueError as e:
    print(f"Invalid age entered: {e}")
user_input = input("Enter your age: ")
check_age(user_input)
# This code defines a function to check if an age is even or odd, and raises an exception for invalid ages.
