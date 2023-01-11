names = [
    "John",
    "Agada",
    "Owoicho",
    "David",
    "Prosper",
    "Oyowo",
    "Elijah",
    "Goodluck",
    "Samuel",
    "Clark",
    "James",
    "Joseph",
    "Ogiji",
    "Peter",
    "Michael",
    "Daniel",
    "Desire",
    "Edoh",
]

intern = input("Enter your first name!\n")

if intern in names:
    print(intern + " " + "is a DevOps intern in lab 6")
elif intern == "Frank" or intern == "frank":
    print("Hi Frank!")
    try:
        passcode = int(input("Please provide your instructor passcode: "))
        if passcode != 2642:
            print("The passcode is incorrect, please try again!")
        else:
            print("Welcome to Lab6, Engineer Frank!")
            exit()
    except ValueError:
        print("Invalid passcode, passcode should be a number")
else:
    print(intern + " " + "is not a DevOps intern. \nCheck the Solution Architech Class")
