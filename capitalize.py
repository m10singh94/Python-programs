def capitalize(s):
    s1 = s[0].upper()
    s1 = s1 + s[1:3]
    s1 = s1 + s[3].upper()
    s1 = s1 + s[4:]
    return s1

print(capitalize('macdonald'))
