# creating functions and passing arguments

mySentence = "loves the color"

color_list = ["pink", "maroon", "emerald", "aqua", "grey"]

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{2} {0} {1}.".format(mySentence, i, name)
        lst.append(msg)
    return lst

#for i in color_list:
#    print(mySentence + i)

def get_name():
    go = True
    while go:
        name = input("What is your name? ")
        if name == "":
            print("You need to provide your name.")
        elif name == "Kenzie":
            print("Kenzie hates anything with a hue.")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()


#lst = color_function("Kenzie")
#for i in lst:
#    print(i)


