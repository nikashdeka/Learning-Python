def oddEven():
    print("Odd or Even!")
    number = int(input("Enter a number of your choice: \n"))
    # check number is odd or even
    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")
