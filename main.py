try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError as ex:
    print("Exeption: ", ex)

print("I'm outside the try block")