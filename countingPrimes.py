# to return the number of primes upto a given number (including the number)
def counting_primes(num):
    count = 0
    flag = 0
    for i in range(2, num + 1):
        for j in range (2, (int)(i/2)+1, 1):
            if(i % j != 0):
                flag = 0
                continue
            else:
                flag = 1
                break
        if(flag == 0):
            count += 1
    return count

print(counting_primes(100))
print(counting_primes(9))