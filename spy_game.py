# return true if the list contains 007 in order
def spy_game(ls):
    mylist = []
    count = 0
    for i in ls:
        if(i == 0 and count < 2):
            mylist.append(i)
            count += 1
        if(i == 7):
            mylist.append(i)
    if(mylist[0] == 0 and mylist[1] == 0 and mylist[2] == 7):
        return True
    else:
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))