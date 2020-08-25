# You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars),
# and the starting inventory. Return the total profit made, rounded to the nearest dollar.
# E.g. profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
#    }) ➞ 14796
# Difficulty: Medium

def profitcalculator(c, s, i):
    profit = (int(s) - int(c)) * int(i)

    return print("Profit({\n cost_price: "+c+"\n sell_price: "+s+"\n inventory: "+i+" \n }) ➞ "+str(profit))


cost_price = input("Please enter the cost price per unit: ")
sell_price = input("Please enter the sell price per unit: ")
inventory = input("Please enter the amount of stock: ")
profitcalculator(cost_price, sell_price, inventory)
