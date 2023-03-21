import random

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# c = []

# #  iterate through list a & b
# for elem in a:
#     if elem in b:
#         c.append(elem)
#     else:
#         continue

# print()
# print(f"List with common integers = {c}")

# print("--------------------------------------------------")

# d = [random.randint(2, 20) for elem in range(10)]
# e = [random.randint(2, 20) for elem in range(10)]
# f = []

# print()
# print(f"Random list 1 = {d}")
# print(f"Random list 2 = {e}")


# for elem in d:
#     if elem in e:
#         f.append(elem)
#     else:
#         continue

# print(f"List wih common integers= {d}")


yourList1 = [random.randint(2, 20) for elem in range(10)]
yourList2 = [random.randint(2, 20) for elem in range(10)]
print(yourList1)
print(yourList2)

def iterate_a_list(yourList1, yourList2):
    overlap_list=[]
    for elem in yourList1:
        if elem in yourList2:
            overlap_list.append(elem)
    return overlap_list

h = iterate_a_list(yourList1= yourList1, yourList2= yourList2)

print(f"List of overlapped integers= {h}")
