def pig_latin(word):
    #if((word[0].lower() == 'a') or (word[0].lower() == 'e') or (word[0].lower() == 'i') or (word[0].lower() == 'o') or (word[0].lower() == 'u')):
    if word[0].lower() in 'aeiou':
        print(word + 'ay')
    else:
        ch = word[0]
        print(word[1:] + ch + 'ay')

pig_latin('apple')
pig_latin('word')
pig_latin('Umbrella')