number = int(input("Enter a number to divide: "))

num = range(5, 50)

rangeList = []
divisorList = []

for elem in num:
    rangeList.append(elem)
    if elem % number == 0: divisorList.append(elem)
      
print(rangeList)
print(divisorList)