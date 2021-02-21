# to print only the words that start with a s in this statement
st = "Print only the words that start with a s in this statement"
list_st = st.split()
#print(list_st)
for word in list_st:
    if(word[0] == 's'):
        print(word)

# to print even numbers from 0 to 10
for num in range(0,11,2):
    print(num)