def check_password_strength():
    password = input("ENTER PASSWORD :")

    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) < 8:
        print("WEAK PASSWORD( ADD MORE CHARACTERS)")
        return
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
    if has_upper and has_lower and has_digit:
        print("PASSWORD IS STRONG")
    else:
        print("PASSWORD IS MEDIUM!")
        print("Tip: use upper case,lowercase and numbers")

def secure_login():
    saved_username = "admin"
    saved_password = "Admin456"

    attempts = 3 

    while attempts > 0:
        username = input("Enter username:")
        password = input("Enter password:")

        if username == saved_username and password == saved_password:
            print("Login successfull!")
            return
        else:
            attempts -=1
            print("Wrong details")
            print("Attempts left:",attempts)
            
while True:
    print("\n---Password Security Tool---")
    print("1.check password strength")
    print("2.Secure Login System")
    print("3.Exit")

    choice = input("Enter your choice:")

    if choice =="1":
        check_password_strength()
    elif choice == "2":
        secure_login()
    elif choice == "3":
        print("Thank you")
        break
    else:
        print("Invalide choice, try again")
