money = 150
trash = {}
z = 0
purchased = {}

#inventory

inventory = {

    "rice": {"quantity": 10, "price": 25},

    "beans": {"quantity": 8, "price": 8},

    "pasta": {"quantity": 15, "price": 5},

    "cookies": {"quantity": 20, "price": 4},

    "chocolate": {"quantity": 12, "price": 6},

    "water": {"quantity": 30, "price": 3},

    "juice": {"quantity": 15, "price": 7},

    "soda": {"quantity": 20, "price": 9},

    "coffee": {"quantity": 10, "price": 12},

    "dish soap": {"quantity": 25, "price": 3},

    "soap": {"quantity": 15, "price": 8},

    "disinfectant": {"quantity": 10, "price": 10},

    "sponge": {"quantity": 30, "price": 2},

    "shampoo": {"quantity": 12, "price": 15},

    "body wash": {"quantity": 25, "price": 4},

    "toothpaste": {"quantity": 18, "price": 7},

    "toilet paper": {"quantity": 20, "price": 15},

    "headphones": {"quantity": 8, "price": 35},

    "charger": {"quantity": 10, "price": 25},

    "batteries": {"quantity": 20, "price": 8},

    "usb cable": {"quantity": 15, "price": 12},

    "notebook": {"quantity": 15, "price": 20},

    "pen": {"quantity": 40, "price": 2},

    "pencil": {"quantity": 30, "price": 1},

    "eraser": {"quantity": 25, "price": 2}
}

#cashier

def cashier(cart, money, z):
   for values in cart.values():
    z = values[1] + z
   if z == 0:
      print("   ")
      purchased = 0
      return money, purchased
   else:
      y = z
      print("total value:", str(z), "R$")
      finalizing_purchase = int(input("Do you wish to complete the purchase? 1-Yes | 2-No"))
      if finalizing_purchase == 1:
        if money < z:
          purchased = 0
          y = 0
          print("insufficient money!")
          return money, purchased, y
        elif money >= z:
          money -= z
        purchased = cart
      else:
           print("Purchase cancelled")
           purchased = 0
      return money, purchased, y

#receipt

def receipt(money, purchased, y):
   if not purchased:
      return money, purchased
   else:
      print("=================RECEIPT=================")
      print("|product:        | quantity:  | price:  |")
      print("|---------------------------------------|")
      for keys, values in purchased.items():
        print(f"|{keys:<15}|  {values[0]:<12}| R$ {values[1]:<4}|")
   print(f"|        Purchase Value: R$ {y:<12}|")
   print("=========================================")
   return money, purchased

# Main program

while True:
 cart = {}
 print("Welcome to the Supermarket")
 print("product:     | quantity:  | price:   ")
 for product, data in inventory.items():
   quantity = data["quantity"]
   price = data["price"]
   print(f"{product:<15} {quantity:<12} R$ {price}")


 while True:
    choice = input("choose an item | 1-Cart | 2-exit  ")
    if choice == "1":
        if not cart:
           print("empty cart")
        else:
         for keys, values in cart.items():
           print(f"item: {keys} | quantity: {values[0]} | price: {values[1]} R$")
         choice_c = input("Do you want to remove any items? Which ones? | 1-exit ")
         if choice_c in cart:
            trash = cart.pop(choice_c)
            print("product removed")
         elif choice_c == "1":
            continue
         elif choice_c not in cart:
            print("This product is not in the cart!")
         else:
            continue
    elif choice == "2":
        if not cart:
           choice_s = input("your cart is empyt! | 1-go back | 2-exit")
           if choice_s == "1":
              continue
           elif choice_s == "2":
              break
           else:
              continue      
        else:
           break
    elif choice in inventory:
        if inventory[choice]["quantity"] == 0:
           print("Product out of stock!")
           continue
        try:
          quantity = int(input("quantity: "))
          if quantity == 0:
             print("It's not possible to buy 0 items!")
             continue
        except ValueError:
           print("Enter only numbers.")
           continue
        choice_e = 0
        if quantity > inventory[choice]["quantity"]:
            print("out of stock")
            choice_e = int(input(f"You only want to add {inventory[choice]["quantity"]} items? 1-Yes | 2-No"))
            if choice_e == 1:
             quantity = inventory[choice]["quantity"]
             print(f"{inventory[choice]["quantity"]} added")
            elif choice_e == 2:
              continue

        price = inventory[choice]["price"] * quantity
        inventory[choice]["quantity"] -= quantity
        if choice not in cart:
            cart[choice] = quantity, price
        elif choice in cart:
            cart[choice] = (
               cart[choice][0] + quantity,
               cart[choice][1] + price
               )
    else:
      print("Product unavailable.")
      continue

#final

 if not cart:
   print("no items purchased")
 elif purchased == 0:
   print("no items purchased")
 else:  
   money, purchased, y = cashier(cart, money, z)
   money, purchased = receipt(money, purchased, y)

#results
  
 print(f"money: {money} R$")
 choice_f = int(input("Do you want to go back to the supermarket? 1-Yes | 2-No"))
 if choice_f == 1:
     quantity = 0
     
     continue
 else:
      break