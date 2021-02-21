# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and a number 
# is '11', reduce the total sum by 10. Finally, if teh sum (even after adjustment) exceeds 21, return 'BUST'

def blackJack(a, b, c):
    if((a <= 11 and a >= 1) or (b <= 11 and b >= 1) or (c <= 11 and c >= 1)):
        sum = a + b + c
        if(sum < 21):
            return sum
        elif (sum > 21 and (a == 11 or b == 11 or c == 11)):
                sum = sum - 10
                if(sum > 21):
                    return 'BUST'
                else:
                    return sum
        else :
            return 'BUST'

print(blackJack(5, 6, 7))
print(blackJack(9, 9, 9))
print(blackJack(9, 9, 11))

    