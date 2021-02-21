# return True if number is within 10 of 100 or 200
def almost_there(num):
    if((abs(num) <= 110 and abs(num) >= 90) or (abs(num) <= 210 and abs(num) >= 190)):
        return True
    else:
        return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print(almost_there(-105))