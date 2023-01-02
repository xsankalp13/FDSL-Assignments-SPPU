'''
Experiment No. 1 : In a second year computer engineering class, group A students play cricket, group B students play
                   badminton and group C students play football.
                   Write a python program using functions to compute following:
                   a) List of students who play both cricket and badminton.
                   b) List of students who play either cricket or badminton but not both.
                   c) Number of students who play neither cricket nor badminton.
                   d) Number of students who play cricket and football but not badminton.
(NOTE : While realising the group, duplicate entries should be avoided. Do not use SET built-in functions)
'''


def intersection(list1,list2):
    list3 =[]
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3

def union(list1,lis2):
    list3= list1.copy()
    for i in list3:
        if i in lis2:
            pass
        else:
            list3.append(i)
    return list3

def symitricdiff(list1,list2):
    list3=[]
    if i in list1:
        if i not in list2:
            list3.append(i)
    return list3

SEcomp =[]
n = int(input("Enter the number of students: "))
for i in range(n):
    while(1):
        a = int(input("Enter the roll number of the student: "))
        if a not in SEcomp:
            SEcomp.append(a)
            break
        else:
            print("Student already present!")

#cricket

cricket=[]
freshstudent = n
m = int(input("Enter the number of students who play cricket: "))
if m>n:
    print("Number of students who play cricket is greater than number of students in the class")
    exit(0)
else:
    freshstudent = n-m
    for i in range(m):
        while(1):

            a = int(input("Enter the roll number of the studets: "))
            if a in SEcomp:
                if a not in cricket:
                    cricket.append(a)
                    break
                else:
                    print("Player already in cricket list")
            else:
                print("given roll number not in SE calss")
                exit(0)

#football
football =[]
m = int(input("Enter the number of students who play football: "))
if m>n:
    print("Number of students who play football is greater than number of students in the class")
    exit(0)
else:
    for i in range(m):
        while(1):
            a = int(input("Enter the roll number of the student: "))
            if a in SEcomp:
                if a not in football:
                    football.append(a)
                    if a in cricket:
                        pass
                    else:
                        freshstudent = freshstudent -1
                break
            else:
                print("given roll number not in SE calss")
                exit(0)
#badminton
badminton=[]
m = int(input("Enter the number of students who play badminton: "))
if m>n:
    print("Number of students who play badminton is greater than number of students in the class")
    exit(0)
else:
    for i in range(m):
        while(1):
            a = int(input("Enter the roll number of Student: "))
            if a in SEcomp:
                if a not in badminton:
                    badminton.append(a)
                    if a in cricket:
                        pass
                    elif a in football:
                        pass
                    else:
                        freshstudent = freshstudent-1
                break
            else:
                print("given roll number not in SE calss")
                exit(0)

CB = intersection(cricket,badminton)
eCeB =symitricdiff(union(cricket,badminton),intersection(cricket,badminton))

nCnB = len(football) + freshstudent

eCeFnB = symitricdiff(union(cricket,football),badminton)
numecefnb = len(eCeFnB)

print(f"list of students who play cricket and badminton both:{CB}")
print(f"List of students who play Either cicket or Badminton but not both: {eCeB}")
print(f"Number of student not play cricket and badminton: {nCnB}")
print(f"4: {numecefnb}")
