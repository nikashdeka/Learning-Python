a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list_of_even_elem = []

# for elem in a:
#     if elem % 2 == 0:
#         list_of_even_elem.append(elem)

list_of_even_elem = [elem for elem in a if elem % 2 == 0]




print(f"List of Even elements: {list_of_even_elem}")