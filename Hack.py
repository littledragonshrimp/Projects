from datetime import date

# food tuples
meattup = ("Beef", "Chicken", "Pork")
veggietup = ("Cabbage", "Corn", " Cucumber", "Eggplant",
             "Spinach", "Mushroom", "Tomato", "Avocado")
roottup = ("Potato", "Carrot", "Onion")
seatup = ("Shellfish", "Fish")

# types of food
meat = {"BEEF": [], "CHICKEN": [], "PORK": []}
veggie = {"CABBAGE": [], "CORN": [], "CUCUMBER": [], "EGGPLANT": [],
          "SPINACH": [], "MUSHROOM": [], "TOMATO": [], "AVOCADO": []}
root = {"POTATO": [], "CARROT": [], "ONION": []}
sea = {"SHELLFISH": [], "FISH": []}

# food compile
food = [meat, veggie, root, sea]


def foodtype():
    clientinp = input("What type of food?\nMeat\nVeggie\nRoot\nSeafood\n>")
    if clientinp.upper() == "MEAT":
        print("\nWhat type of meat?")
        for i in meattup:
            print(i)
        secondinp = input(">")
    if clientinp.upper() == "VEGGIE":
        print("\nWhat type of veggie?")
        for i in veggietup:
            print(i)
        secondinp = input(">")
    if clientinp.upper() == "ROOT":
        print("\nWhat type of root?")
        for i in roottup:
            print(i)
        secondinp = input(">")
    if clientinp.upper() == "SEAFOOD":
        print("\nWhat type of seafood?")
        for i in seatup:
            print(i)
        secondinp = input(">")
    return clientinp.upper(), secondinp


def quantity():
    quantinp = input("How many?\n>")
    num = int(quantinp)
    return num


# date
time = date.today()

# shelf life
expirations = {"BEEF": 4,
               "CHICKEN": 4,
               "PORK": 4,
               "CABBAGE": 30,
               "CORN": 4,
               "CUCUMBER": 10,
               "EGGPLANT": 11,
               "SPINACH": 11,
               "MUSHROOM": 7,
               "TOMATO": 5,
               "AVOCADO": 10,
               "POTATO": 60,
               "CARROT": 45,
               "ONION": 60,
               "SHELLFISH": 1,
               "FISH": 1}


# def client():

print(time)
