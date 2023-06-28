#Input for the price of the item on https://www.csgoroll.com/en/withdraw/csgo/p2p
rollprice = input("price: ")

#Converts the price on csroll to USD
dollarprice = float(rollprice) * 0.70

#Converts USD to GBP
poundprice = float(dollarprice) * 0.81

#Prints price in pounds
print("£",poundprice)