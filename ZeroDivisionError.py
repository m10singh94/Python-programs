x = 5
y = 0
try:
    print(x/y)
except ZeroDivisionError:
    print("An error occurred. Division by zero not possible")
finally:
    print("All done")