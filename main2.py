try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter a numarical value")
except NameError as ex:
    print("The Exception: ", ex)
except:
    print("Some error occurred")
finally:
    print("I will execute no matter what happens")