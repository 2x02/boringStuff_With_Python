print("How many cats you have?")
try:
    numCats = input()
    if int(numCats) >= 4:
        print("Wow, thats a lot")
    else:
        print("This in not a lot")
except ValueError:
    print("You did not enter a number")
    
