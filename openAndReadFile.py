with open('text.txt') as new_file:
    print(new_file.read())
with open('text.txt', mode = 'a') as new_file:
    new_file.write("\nWhy don't you come here!")
