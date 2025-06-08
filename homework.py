try:
    age_input = input("Enter your age: ")
    age = int(age_input)
    if age < 0 or age > 150:
        print("Error: Please enter a realistic age between 0 and 150.")
    else:
        if age % 2 == 0:
            print("The age entered is even.")
        else:
            print("The age entered is odd.")
except ValueError:
    print("Value Error: Please enter a valid integer for age.")