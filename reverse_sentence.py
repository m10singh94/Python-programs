def reverse_sentence(s):
    s1 = s.split()
    s = s1[-1]
    for item in range(len(s1) - 2, -1, -1):
        s = s + ' ' + s1[item]
    return s

print(reverse_sentence('I am home'))
print(reverse_sentence('We are ready'))
        