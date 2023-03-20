a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

number = int(input("Enter a number: "))

b = []

for elm in a:
    if elm < number: b.append(elm)
print(b)

# one-liner
print([elm for elm in a if elm < number])

