def frequency():
    highfrequency = 0
    marks = 0
    for i in range(totalNumberOfStudents):
        if listOfMarks[i] == "ab":
            pass
        else:
            temp = listOfMarks.count(listOfMarks[i])
            if temp > highfrequency:
                highfrequency = temp
                marks = listOfMarks[i]
    return marks

def absent():
    return listOfMarks.count("ab")

def lowest():
    lowestmarks = 1000000
    for i in range(totalNumberOfStudents):
        if listOfMarks[i] == "ab":
            pass
        else:
            if lowestmarks>listOfMarks[i]:
                lowestmarks = listOfMarks[i]
    return listOfMarks.index(lowestmarks)

def highest():
    highestmarks = 0
    for i in range(totalNumberOfStudents):
        if listOfMarks[i] == "ab":
            pass
        else:
            if highestmarks<listOfMarks[i]:
                highestmarks = listOfMarks[i]
    return listOfMarks.index(highestmarks)

def avgScore():
    marks = 0
    for i in range(totalNumberOfStudents):
        if listOfMarks[i] == "ab":
            pass
        else:
            marks = marks + listOfMarks[i]
    avg = marks / (totalNumberOfStudents)
    return avg

def getMarks(i):
    marks = input(f"Enter the marks of {listOfNames[i]} : ")
    if marks == "ab":
        listOfMarks.append(marks)
    else:
        listOfMarks.append(int(marks))

def getName():
    name = input("Enter the name of the student: ")
    listOfNames.append(name)

listOfNames = []
listOfMarks = []
totalNumberOfStudents = int(input("Enter the total number of students: "))
for i in range(totalNumberOfStudents):
    getName()
    getMarks(i)
averageScore = avgScore()
print("Average score of the class is : ", averageScore)
highestScore = listOfMarks[highest()]
lowestScore = listOfMarks[lowest()]
print("Highest score of the class :", highestScore, "Scored by ",listOfNames[highest()], "\n and Lowest score of the class is :", lowestScore, "scored by ", listOfNames[lowest()])
print("The number of students were absent for the test : ", absent())
print("The highest frequency is :", listOfMarks.count(frequency()), "for the marks :", frequency())