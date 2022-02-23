"""
Name: Tennessee Tremain
Program: Restaurant
"""

cont = "yes"

while cont.lower().startswith("y"):
    
    vegetarian = False
    vegan = False
    gluten = False

    inp = input("Is anyone in your party a vegetarian?\n")
    if inp.lower() == "yes":
        vegetarian = True

    inp = input("Is anyone in your party a vegan?\n")
    if inp.lower() == "yes":
        vegan = True

    inp = input("Is anyone in your party gluten-free?\n")
    if inp.lower() == "yes":
        gluten = True

    if vegan:
        print("Here are your restaurant choices:" +
        "\nCorner Café\nThe Chef's Kitchen")
    elif gluten:
        print("Here are your restaurant choices:" +
        "\nMain Street Pizza Company\nCorner Café\nThe Chef's Kitchen")
    elif vegetarian:
        print("Here are your restaurant choices:" +
            "\nMain Street Pizza Company\nCorner Café\nMama's Fine Italian\nThe Chef's Kitchen")
    else:
        print("Here are your restaurant choices:" +
            "\nJoe's Gourmet Burgers\nMain Street Pizza Company\nCorner Café\nMama's Fine Italian\nThe Chef's Kitchen")
   
    cont = input("Enter \'yes\' if you would like to do another restaurant search (enter \'no\' to end): ")
    
    while not(cont.lower().startswith("y")) and not(cont.lower().startswith("n")):
        cont = input("ERROR!  TRY AGAIN: ")
    
print("Thanks, goodbye!")
