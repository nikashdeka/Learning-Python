def user():
    names = ["Nick", "Dia", "Nikash", "Diana"]

    name = input("Enter your name: \n")
    # Check the length of the name entered
    while len(name) < 3:
        name = input("Please enter a valid name: \n")
    else:
        return name
