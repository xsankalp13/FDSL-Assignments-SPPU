def xyz():
    cb = []
    for i in cricket and football:
        if i not in badminton:
          cb.append(i)
    return cb


def cricketplayfootballplay():
    cb = []
    for i in range(len(cricket)):
        for j in range(len(football)):
            if(cricket[i] == football[j]):
                cb.append(football[j])
    print(cb)
    for i in range(len(badminton)):
        for j in range(len(cb)):
            if(cb[j] == badminton[i]):
                cb.remove(badminton[i])
    return cb



def cricketintersectionBadminton():
    playersIncricket = len(cricket)
    playersInBadminton = len(badminton)
    cnb = []
    for i in range(playersIncricket):
        for j in range(playersInBadminton):
            if(cricket[i] == badminton[j]):
                cnb.append(badminton[j])
    return cnb

def cricketUnionBadminton():
    cud = []
    for i in range(len(cricket)):
        cud.append(cricket[i])
    for i in range(len(badminton)):
        cud.append(badminton[i])
    cnd = cricketintersectionBadminton()
    for i in range(len(cnd)):
        cud.remove(cnd[i])
        cud.remove(cnd[i])
    return cud


total_num = int(input("Enter the total number of students: "))

cricket = []
badminton =[]
football=[]
count = 0
while(1):
    temp = input(" Input for Cricket: ")
    if(temp == 'n'):
        break
    elif(count >total_num):
        print("This is not Valid")
        break
    else:
        cricket.append(temp)
        count +=1
count = 0
while(1):
    temp = input(" Input for Badminton: ")
    if(temp == 'n'):
        break
    elif(count >total_num):
        print("This is not Valid")
    else:
        badminton.append(temp)
        count +=1
count = 0
while(1):
    temp = input(" Input for Football: ")
    if(temp == 'n'):
        break
    elif(count >total_num):
        print("This is not Valid")
    else:
        football.append(temp)
        count +=1

cnb = cricketintersectionBadminton()
# print(cricket)
# print(badminton)
# print(football)
print("Players who play Cricket and Badminton Both: ", cnb)
cub = cricketUnionBadminton()
print("Players who plays either cricket or Badminton: ", cub)
print("Players who play neither cricket nor badminton ", football)
cf = xyz()
print("Players who play cricket and football but not badminton", cf)