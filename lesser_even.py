def myfunc(num1, num2):
    if((num1 % 2 == 0) and (num2 % 2 == 0)):
        if(num1 < num2): # return min(num1,num2)
            return num1
        else: 
            return num2
    else:
        if(num1 > num2): # return max(num1,num2)
            return num1
        else:
            return num2

print(myfunc(2,4))
print(myfunc(2,5))