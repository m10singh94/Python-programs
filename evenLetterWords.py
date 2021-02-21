# printing words with even number of letters
st = 'Print every word in this sentence that has an even number of letters'
myList = st.split()
for word in myList:
    count = len(word)
    if (count % 2 == 0):
        print(word)