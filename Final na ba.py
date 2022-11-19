import datetime
import random

attempts = 0
Username = "1"
Password = "2"
while attempts < 5:     # Loop for Log In
    attempts = attempts + 1
    Username1 = input("Username: ")
    Password1 = input("Password: ")
    if Password1 == Password and Username == Username1:
        from array import *

        main = True
        while main:     # Loop if order is Done
            print("Welcome User")
            # Flavors
            flavors = ["", "Mild Yangnyeom", "Spicy Yangnyeom", "Garlic Parmesan", "Jack Daniel's", "Garlic Soy",
                       "Garlic Ranch", "Sriracha", "Sweet & Sour", "Gravy", "Salted Egg", "Snow Cheese", "Original"]
            # BLENDED DRINKS
            drinks = ["Chocolate", "Dark Choco Mocha", "Frappuccino", "Oreo"]
            prices = [55, 55, 55, 65]
            # FRESH LEMONADES
            fresh_lemonades = ["Classic", "Cucumber", "Mixed Berries"]
            fresh_prices = [55, 55, 55]
            # EXTRAS
            extras = ["Rice", "Kimchi", "Rice Meal", "1 Dozen (with kimchi)", "2 Dozens (with kimchi)"]
            extras_prices = [15, 25, 68, 180, 350]

            arr = array('i', [])  # Store Pieces
            order_item = []  # Store Order Items
            order_prices = []  # Store Order Prices
            order_flavor = []  # Store Order flavor
            over_total = 0

            next_order = True
            while next_order:     # Loop for adding more items
                print("MENU \n1 - BLENDED DRINKS \n2 - FRESH LEMONADES \n3 - EXTRAS")
                menu = int(input("What do you want to order?: "))
                if menu == 1:   # BLENDED DRINKS STATEMENTS
                    print("1 - Chocolate \n2 - Dark Choco Mocha \n3 - Frappuccino \n4 - Oreo")
                    order = int(input("What's your order?: "))
                    if order == 1:
                        order_item.append(drinks[0])
                        order_prices.append(prices[0])
                        how_many = int(input("How many?: "))
                        arr.append(how_many)
                        total = how_many * (prices[0])
                        over_total = over_total + total
                        order_flavor.append(flavors[0])
                    elif order == 2:
                        order_item.append(drinks[1])
                        order_prices.append(prices[1])
                        how_many = int(input("How many?: "))
                        arr.append(how_many)
                        total = how_many * (prices[1])
                        over_total = over_total + total
                        order_flavor.append(flavors[0])
                    elif order == 3:
                        order_item.append(drinks[2])
                        order_prices.append(prices[2])
                        how_many = int(input("How many?: "))
                        arr.append(how_many)
                        total = how_many * (prices[2])
                        over_total = over_total + total
                        order_flavor.append(flavors[0])
                    elif order == 4:
                        order_item.append(drinks[3])
                        order_prices.append(prices[3])
                        how_many = int(input("How many?: "))
                        arr.append(how_many)
                        total = how_many * (prices[3])
                        over_total = over_total + total
                        order_flavor.append(flavors[0])
                    else:
                        print("Not in the list")
                elif menu == 2:     # FRESH LEMONADES STATEMENTS
                    print("1 - Classic \n2 - Cucumber \n3 - Mixed Berries")
                    order1 = int(input("What's your order?: "))
                    if order1 == 1:
                        order_item.append(fresh_lemonades[0])
                        order_prices.append(fresh_prices[0])
                        how_many = int(input("How many?: "))
                        arr.append(how_many)
                        total = how_many * (fresh_prices[0])
                        over_total = over_total + total
                        order_flavor.append(flavors[0])
                    elif order1 == 2:
                        order_item.append(fresh_lemonades[1])
                        order_prices.append(fresh_prices[1])
                        how_many = int(input("How many?: "))
                        arr.append(how_many)
                        total = how_many * (fresh_prices[1])
                        over_total = over_total + total
                        order_flavor.append(flavors[0])
                    elif order1 == 3:
                        order_item.append(fresh_lemonades[2])
                        order_prices.append(fresh_prices[2])
                        how_many = int(input("How many?: "))
                        arr.append(how_many)
                        total = how_many * (fresh_prices[2])
                        over_total = over_total + total
                        order_flavor.append(flavors[0])
                    else:
                        print("Not in the list")
                elif menu == 3:     # EXTRAS STATEMENTS
                    print(
                        "1 - Rice \n2 - Kimchi \n3 - Rice Meal \n4 - 1 Dozen(with kimchi) \n5 - 2 Dozens(with kimchi)")
                    order2 = int(input("What's your order?: "))
                    if order2 == 1:
                        order_item.append(extras[0])
                        order_prices.append(extras_prices[0])
                        how_many = int(input("How many?: "))
                        arr.append(how_many)
                        total = how_many * (extras_prices[0])
                        over_total = over_total + total
                        order_flavor.append(flavors[0])
                    elif order2 == 2:
                        order_item.append(extras[1])
                        order_prices.append(extras_prices[1])
                        how_many = int(input("How many?: "))
                        arr.append(how_many)
                        total = how_many * (extras_prices[1])
                        over_total = over_total + total
                        order_flavor.append(flavors[0])
                    elif order2 == 3:
                        order_item.append(extras[2])
                        order_prices.append(extras_prices[2])
                        how_many = int(input("How many?: "))
                        arr.append(how_many)
                        total = how_many * (extras_prices[2])
                        over_total = over_total + total
                        print("Flavors:\n1- Mild Yangnyeom \n2- Spicy Yangnyeom \n3- Garlic Parmesan \n4- Jack "
                              "Daniel's \n5- "
                              "Garlic Soy \n6- Garlic Ranch \n7- Sriracha \n8- Sweet & Sour \n9- Gravy \n10- Salted "
                              "Egg \n11- "
                              "Snow Cheese \n12- Original")
                        chicken_flavor = int(input("Chicken Flavor: "))
                        order_flavor.append(flavors[chicken_flavor])
                    elif order2 == 4:
                        order_item.append(extras[3])
                        order_prices.append(extras_prices[3])
                        over_total = over_total + extras_prices[3]
                        arr.append(0)
                        print("Flavors:\n1- Mild Yangnyeom \n2- Spicy Yangnyeom \n3- Garlic Parmesan \n4- Jack "
                              "Daniel's \n5- "
                              "Garlic Soy \n6- Garlic Ranch \n7- Sriracha \n8- Sweet & Sour \n9- Gravy \n10- Salted "
                              "Egg \n11- "
                              "Snow Cheese \n12- Original")
                        chicken_flavor = int(input("Chicken Flavor: "))
                        order_flavor.append(flavors[chicken_flavor])
                    elif order2 == 5:
                        order_item.append(extras[4])
                        order_prices.append(extras_prices[4])
                        how_many = int(input("How many?: "))
                        arr.append(how_many)
                        total = how_many * (extras_prices[4])
                        over_total = over_total + total
                        print("Flavors:\n1- Mild Yangnyeom \n2- Spicy Yangnyeom \n3- Garlic Parmesan \n4- Jack "
                              "Daniel's \n5- "
                              "Garlic Soy \n6- Garlic Ranch \n7- Sriracha \n8- Sweet & Sour \n9- Gravy \n10- Salted "
                              "Egg \n11- "
                              "Snow Cheese \n12- Original")
                        chicken_flavor = int(input("Chicken Flavor: "))
                        order_flavor.append(flavors[chicken_flavor])
                    else:
                        print("Not in the list")
                else:
                    print("Not in the Menu List")
                add1 = True
                while add1:     # Loop for adding more Items
                    add = input("Do you want to add more? Y/N: ")
                    if add == "Y":
                        add1 = False
                        next_order = True
                    elif add == "N":
                        special_orders = input("Special Orders: ")  # Cashier Only
                        next_order = False
                        print("\n")
                        print("         Chicken Chicken",
                              "\n         CHICKEN CHICKEN")
                        print("Cashier: Owner")
                        print("POS: POS 1")
                        print("........................")
                        [print(z, "x", x, "-", y, w)
                         for (z, x, y, w) in zip(arr, order_item, order_prices, order_flavor)]
                        print("Special Orders:", special_orders)
                        print("........................")
                        print("Total", over_total)
                        print("   ")
                        payment = True
                        while payment:      # Loop for payment
                            cos_money = int(input("Cash:      "))
                            if cos_money < over_total:
                                change = cos_money - over_total
                                print("Customer is lack of payment of", change)
                                payment = True
                            else:
                                change = cos_money - over_total
                                print("Change:   ", change)
                                print("........................")
                                print("PHINMA-Cagayan de Oro College \nCarmen, Cagayan de Oro City")
                                time = datetime.datetime.now()
                                print(time.strftime("%m-%d-%y     %H:%M:%S%p"), "#1-", random.randrange(1000, 5000))
                                print("\n")
                                payment = False
                                main = True
                        add1 = False
                    else:
                        print("Y for Yes and N for No only")
                        add1 = True
    elif Password1 != Password and Username1 == Username:
        print("Password Incorrect")
    elif Username != Username1 and Password1 == Password:
        print("Username Incorrect")
    else:
        print("User not found")
