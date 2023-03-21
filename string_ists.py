str = input("Enter a string: ").lower()

def isPalindrome(str):
  return str == str[::-1]

result = isPalindrome(str)
print(result)
print(f"Yes, {str} is a Palindrome" if result  else f"No, {str} is not a Palindrome")
# if result:
#   print("Yes")
# else:
#   print("No")
