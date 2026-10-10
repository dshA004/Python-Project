pwd = input("What is the master password? ")

def view():
    pass


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break 
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode.")
        continue