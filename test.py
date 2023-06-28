#--------------Lesson 1


#print("hello world")
#print("i am iron man")
#print("no, i am tony stark")
#print("no, i am poppy")
#we are practising python, its awsome


#print("""i am iron man. 
#no, i am iron man. 
#no i am poppy""")

#print("i am iron man. \n" + "no, i am tony stark. \n" + "no, i am poppy")

#print("i am poppy.\n" * 100)


#--------------Lesson 2


#lets build a barista!!

#print("hello welcome to lukes coffee!!!!!!!!")

#name = input("what is your name?\n")

#print("hello " + name + ", thank you so much for coming in today.\n\n")

#drink = input("please choose an item from our menu:\n-black coffee\n-white coffee\n-green coffee\n-blue coffee\n")

#print("ok " + name + " youre " + drink + " will be ready in a moment")

#menu = "black coffee, espresso, latte, cappucino"

#print(name + ", what wpuld you like from our menu today? here is what we are serving.\n" + menu)

#order = input()

#print("sounds good " + name + ", we'll have that " + order + " ready for you in a moment.")


#name = "Luke"

#print(name)

#name = "ironman"

#print(name)


#--------------lesson 3


#lets play with some numbers

#name = "luke"

#age = 18

#actual_age = 18.60

#print(name)

#print(age)

#print(type(name))

#print(type(age))

#print(type(actual_age))

#maths = 5 ** 7 + 6 / 9 * 6 - 4

#resaults = age + actual_age + maths

#print(resaults)


#print("hello welcome to lukes coffee!!!!!!!!")

#name = input("what is your name?\n")

#print("hello " + name + ", thank you so much for coming in today.\n\n")

#drink = input("please choose an item from our menu:\n-black coffee\n-white coffee\n-green coffee\n-blue coffee\n")

#amount = input("ok " + name + " how much " + drink + " would you like?\n")

#coffeeprice = 8

#totalprice = coffeeprice * int(amount)

#print("ok " + name + " that comes to £" + str(totalprice))

#print(name + ", Your " + amount + " " + drink + " will be ready in a moment")

#input()


#--------------Lesson 4


#print("hello welcome to lukes coffee!!!!!!!!")

#name = input("what is your name?\n")

#if name == "ben":
#    print("you are not welcome here Evil ben!! get out!!") 
#    exit()
#else:
#    print("hello " + name + ", thank you so much for coming in today.\n\n")

#beard = input("do you have a beard?\n")

#if beard == "yes":
#    length = input("brilliant! how long is it?\n")
#    if int(length) > 1:
#        print("amazing come to the front!")
#    else:
#        print("unfortunate")
#else:
#    print("unfortunate")

#drink = input("please choose an item from our menu:\n-black coffee\n-white coffee\n-green coffee\n-blue coffee\n-frappaccino\n")

#if drink =="frappaccino":
#    coffeeprice = 13
#else:
#    coffeeprice = 8

#amount = input("ok " + name + " how much " + drink + " would you like?\n")

#totalprice = coffeeprice * int(amount)

#print("ok " + name + " that comes to £" + str(totalprice))

#print(name + ", Your " + amount + " " + drink + " will be ready in a moment")

#input()

#frappaccinoprice = 13

#if drink == "frappaccino":
#    frappaccinoamount = input("ok " + name + " how much " + drink + " would you like?\n")
#    totalpricefrapp = frappaccinoprice * int(frappaccinoamount)
#    print("ok " + name + " that comes to £" + str(totalpricefrapp))
#    print(name + ", Your " + frappaccinoamount + " " + drink + " will be ready in a moment")
#    input()
#else:
#    amount = input("ok " + name + " how much " + drink + " would you like?\n")
#    totalprice = coffeeprice * int(amount)
#    print("ok " + name + " that comes to £" + str(totalprice))
#    print(name + ", Your " + amount + " " + drink + " will be ready in a moment")
#    input()

#amount = input("ok " + name + " how much " + drink + " would you like?\n")

#totalprice = coffeeprice * int(amount)

#print("ok " + name + " that comes to £" + str(totalprice))

#print(name + ", Your " + amount + " " + drink + " will be ready in a moment")

#input()

#if 2 > 3:
#    print("yep it true")
#    print("its still true")
#else:
#    print("nope, its not true")


#--------------Lesson 5


#print("hello welcome to lukes coffee!!!!!!!!")

#name = input("what is your name?\n")

#if name == "ben":
#    evil_status = input("are you evil?\n")
#    if evil_status == "yes":
#        print("you are not welcome here Evil ben!! get out!!") 
#        exit()
#    else:
#        print("oh, so youre one of the good bens. come on in")
#else:
#    print("hello " + name + ", thank you so much for coming in today.\n\n")


#--------------Lesson 6


print("hello welcome to lukes coffee!!!!!!!!")

name = input("what is your name?\n")

if name == "ben" or name == "patricia" or name == "loki":
    evil_status = input("are you evil?\n")
    gooddeed = input("hmmm...ok, how many good deeds have you done today?\n")
    if evil_status == "yes" and int(gooddeed) < 4:
        print("we dont like evil, GETOUT!!\n\n")
        exit()
    else:
        print("well i suppose you cant be all that bad, come on in!")
else:
    print("hello " + name + ", thank you so much for coming in today.\n\n")

beard = input("do you have a beard?\n")

if beard == "yes":
    length = input("brilliant! how long is it?\n")
    if int(length) > 1:
        print("amazing come to the front!")
    else:
        print("unfortunate")
else:
    print("unfortunate")

drink = input("please choose an item from our menu:\n-black coffee\n-white coffee\n-green coffee\n-blue coffee\n-frappaccino\n")

if drink =="frappaccino":
    coffeeprice = 13
else:
    coffeeprice = 8

amount = input("ok " + name + " how much " + drink + " would you like?\n")

totalprice = coffeeprice * int(amount)

print("ok " + name + " that comes to £" + str(totalprice))

print(name + ", Your " + amount + " " + drink + " will be ready in a moment")

input()


#--------------Lesson 7


#campstuff = ("tent, sleeping bags, water, raspeberry pi, coffee, knife, ethernet cable, flash drive, marshmellows")

#print (campstuff)


#list


#campinglist = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "marshmellows"]

#campsite = ["crystal lake", 404, 89.3, True]

#net = campinglist[4]

#me = campinglist [-2]

#print(net)
#print(me)

#print(campinglist)


#--------------Lesson 8



#campinglist = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "marshmellows"]

#campsite = ["crystal lake", 404, 89.3, True]

#campinglist.append("toilet paper") 

#campinglist.append("bidet")

#campinglist.extend(["bidet", "toilet paper"])

#campinglist = campinglist + ["toilet paper", "bidet"]

#campinglist.insert(0, "bidet")

#campinglist.insert(-1, "toilet paper")

#print (campinglist)


#--------------Lesson 9


#campinglist = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "marshmellows"]


#campsite = ["crystal lake", 404, 89.3, True]


#campinglist.extend(["bidet", "toilet paper"])

#campinglist.clear()

#campinglist.remove("tent")

#campinglist.remove("sleeping bags")

#print("this item was just deleted: " + campinglist.pop(0))

#campinglist.pop(0)

#print(campinglist)
