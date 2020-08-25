import os
print("\nHello welcome to the program ")
option = True
while option:
    print("""
        1. ping
        2. neofetch
        3. ifconfig
        4. exit""") 
    option = input("\nChoose an operation:")
    os.system("clear")
    if option == "1":
        os.system("\nping -c 3 localhost")
    elif option == "2":
        os.system("\nneofetch")
    elif option == "3":
        os.system("\nifconfig wlp6s0")
    elif option == "4":
        break
    elif option !="":
        print("\n Not a valid choice, Try again")
    continue
    
