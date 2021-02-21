# ask for an integer
def ask():
    while True:
        try:
            result = int(input("Enter a number : "))
        except:
            print("Entered character is not a number\n")
            continue
        else:
            print(f"the square of {result} is {result**2}")
            break
ask()