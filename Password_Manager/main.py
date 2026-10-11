master_pwd = input("What is the master password? ")


def view():
    try:
        with open("passwords.txt", "r") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print("No passwords saved yet.")
        return

    if not passwords:
        print("No passwords saved yet.")
        return

    for entry in passwords:
        print(entry)


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(f"{name}: {pwd}\n")


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