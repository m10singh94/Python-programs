import random
#1
def gensquares(n):
    for x in range(n):
        yield x**2

for number in gensquares(10):
    print(number) 
print('\n')

#2
def rand_num(low, high, n):
    for i in range(0,n):
        yield random.randint(low,high)
for number in rand_num(1,10,12):
    print(number)
print('\n')

#3
s = 'hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))