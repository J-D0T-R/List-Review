### Lists Review ###
### James Rutley ###
### Start Date: 10/62021 ###
### End Date:

# lists
stock = ["Apples", "Oranges", "Milk", "Eggs", "Cheese", "Chocolate", "Blueberries"]

prices = [5.99, 4.99, 3.99, 3.99]

cart = []

# functions #
def editing():
    edit = input("Are you happy with your purchase?(y/n) ")
    if "y" in str(edit):
        print("Here's your list:")
        print(cart)
        pass
    # removing the item from their list
    else:
        cut_out = input("What do you want to get rid of?" )
        if cut_out in cart:
            cart.remove(cut_out)
            print("Here's your new list")
            print(cart)
            editing()
        else:
            print("Sorry, I can't find that in your cart. Maybe you removed it already?")
            editing()
                    
def shopping():
    add_to_cart = input("What would you like to buy?" )
    if add_to_cart in stock:
        cart.append(add_to_cart)
        keep_shopping = input("Would you like to keep shopping?(y/n) ")
        # checks if they're done
        if "y" in str(keep_shopping):
            shopping()
        else:
            print("Here's what you bought")
            print(cart)
            editing()
           
    else:
        print("Sorry, we don't have that in stock.")
        shopping()
    
    

print("Welcome to the store, here's what we have in stock!")
print(stock)
shopping()
        