valid = False

while not valid:
    try:
        n = int(input("Enter a number: "))
        #enter a even number
        while n%2 == 0:
            print("⭕")
            valid = True

    except ValueError:
        print("Invalid")