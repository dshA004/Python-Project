master_pwd = input("What is the master password? ")

def view():
    pass


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")
        # always use "w" mode if always want to overide a file that potentially already exist
        # "r" mode is simply read mode
        # "a" mode append mode, allow to add something to the end of an existing file, and create a new file if that file doesn't exist,
        # if password on passwords.txt already exist we can write into the file and read the entire file 

    

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break 

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue