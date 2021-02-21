def animal_crackers(s):
    my_list = s.split()
    if(my_list[0][0].lower() == my_list[1][0].lower()): # return my_list[0][0].lower() == my_list[1][0].lower()
        return True
    else:
        return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('crazy Cat'))
print(animal_crackers('Crazy Kangaroo'))
