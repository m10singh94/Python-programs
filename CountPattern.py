def laughter(s, sentence):
    count = 0
    laugh = 0
    for letter in sentence:
        if(letter == s[0]):
            if(sentence[count : count + len(s)] == s):
                laugh += 1
        count += 1
    return laugh

print(laughter('hah','hahahah'))
print(laughter('ha', 'hahahah'))
print(laughter('son', 'sonnnnsongfso'))
