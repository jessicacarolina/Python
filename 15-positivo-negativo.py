def pos_neg():
    number = int(input("Number: "))
    if number > 0:
        return print("Number positive!")
    elif number == 0:
        return print("Number = 0")
    else:
        return print("Number negative!")

pos_neg()