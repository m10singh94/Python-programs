# return a list of numbers which are even by passing numbers as arguments using *args
def myfunc(*args):
    return [x for x in args if(x%2)==0]

s = myfunc(5,6,7,8)
print(s)