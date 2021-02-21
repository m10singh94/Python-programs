def myfunc(st):
    for i in range(0, len(st)):
        if(i == 0):
            s = st[i].upper()
        elif ((i % 2) == 0):
            s = s + st[i].upper()
        else:
            s = s + st[i].lower()
    return s

print(myfunc('ufweIHDNiohHj'))