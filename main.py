import char_input
import odd_or_even

userName = "Nikash"

name =  char_input.user()

if name != userName:
    print("Sorry, wrong user name!")
    print("Please enter correct user name!")
    char_input.user()
else:
    print(f"Welcome, {userName}")
    odd_or_even.oddEven()

# print(f"Congratulations {userName}, you are logged in.")
