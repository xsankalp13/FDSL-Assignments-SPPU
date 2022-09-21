def count():
    cnt = 0
    newlist=[]
    for i in range(len(listOfSortedPrices)):
        temp = listOfSortedPrices[i]
        if temp[1] > 500:
            cnt +=1
            newlist.append(temp[0])
    print(f"{cnt} Books cost more than 500rs.")
    return newlist
def bubbleSort():
    my_list = list(books.items())
    for mx in range(len(my_list) - 1, -1, -1):
        swapped = False
        for i in range(mx):
            if my_list[i][1] < my_list[i + 1][1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                swapped = True
        if not swapped:
            break
    my_list.reverse()
    return my_list

def deleteEntry():
    newdect={}
    for key,value in books.items():
        if key not in newdect.keys():
            newdect[key]=value
    return newdect
def getData(i):
    name = input("Enter the name: ")
    price = float(input(f"Enter the price of {name}: "))
    books[name]=price

books ={}
numberOfbooks=int(input("Enter the total number of books: "))
for i in range(numberOfbooks):
    getData(i)
books = deleteEntry()
print(books)
listOfSortedPrices = bubbleSort()
print("Books in ascending order as per prices: ",listOfSortedPrices)
morethan500 = count()
print("List of books cost more than 500: ",morethan500)
