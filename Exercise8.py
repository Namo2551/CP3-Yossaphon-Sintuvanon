usernameInput = input("username : ")
passwordInput = input("password : ")
if usernameInput == "Namo":
    if passwordInput == "123":
        print("Welcome to Namo shop")
        print("--------------------------------")
        print("Apple  30 THB")
        print("Banana 20 THB")
        print("Namo candy 25 THB")
        buy = input("What do you want to buy : ")
        amount = int(input("how many : "))
        if buy == "Apple":
            print("price is :",amount * 30)
        elif buy == "Banana":
            print("price is :",amount * 20)
        elif buy == "Namo candy":
            print("price is :",amount * 25)
        else:
            print("error ! ")
    else:
        print("password incorrect !")
else:
    print("username incorrect !")