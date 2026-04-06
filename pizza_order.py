# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================
# ----- Menu Data (do not modify) -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions", "Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50 # each topping, any size
# ----- Order Storage -----
order_descriptions = [] # e.g., "Large Pepperoni, Mushrooms"
order_prices = [] # e.g., 15.99
# Your code goes below this line.
size_choices = []

print("==============================")
print("         PIZZA SIZES")
print("==============================")
for i in range(len(sizes)):
    print(f"{i+1}. {sizes[i]:<15}     ${size_prices[i]:>5}")
print("==============================")

# EXERCISE 2 — Get a valid size choice
# Your code here
while True:
    while True:
        try:
            size_choice = int(input("Pick a size (1-4): "))
            if (1 <= size_choice) & (size_choice <= 4):
                base_price = size_prices[size_choice-1]
                size_choices.append(size_choice-1)
                break
            else:
                print("Choose 1-4.")
        except:
            print("Please enter a number!")
        continue

    # EXERCISE 3 — Add toppings
    selected_toppings = []
    # Display available toppings using a for loop
    # Your code here
    print("Available toppings ($1.50 each):")
    for i in range(len(topping_names)):
        print(f"{i+1}. {topping_names[i]}")
    # Topping selection loop (sentinel: "done")
    # Your code here

    print("\n")
    while True:
        try:
            topping = input("Add topping # (or 'done'): ")
            topping_int = int(topping)
            if (1 <= topping_int) & (topping_int <= 8):
                if topping_names[topping_int - 1] in selected_toppings:
                    print(f"Already added {topping_names[topping_int - 1]}")
                else:
                    selected_toppings.append(topping_names[topping_int - 1])
                    print(f"✓ Added {topping_names[topping_int - 1]}")
            else:
                print("Choose 1-8.")
        except:
            if topping == "done" or "Done":
                break
            else:
                print("Please enter a number!")
        continue
    print(selected_toppings)

    # EXERCISE 4 — Calculate price and store the pizza
    order = []
    price = base_price + (len(selected_toppings) * topping_price)
    order.append(sizes[size_choice -1])
    order.append(selected_toppings)
    order_descriptions.append(order)
    order_prices.append(price)

    # EXERCISE 5 — Wrap everything in a multi-pizza loop
    # while True:
    # (Exercise 1 — display menu)
    # (Exercise 2 — choose size)
    # (Exercise 3 — add toppings)
    # (Exercise 4 — calculate and store)
    #
    # Ask "Order another?" with validation
    # If no, break
    
    another = input("Order another pizza? (yes/no): ").lower()
    if another == "no" or another == "n":
        break
    else:
        while True:
            if another == "no" or another == "n":
                break
            elif another == "yes" or another == "y":
                print("Another pizza ordered")
                break
            else:
                print("Enter valid answer")
                another = input("Order another pizza? (yes/no): ").lower()
    if another == "no" or another == "n":
        break

# EXERCISE 8 — Discount code with attempt limit
attempt = 0
discount = 0
while True: 
    if attempt == 3:
        break
    code = input("Do you want to input a discount code?")
    if code == "none":
        print("No discount applied")
        break
    elif code == "STUDENT10":
        discount = .1
        print("Discount applied")
        break
    elif code == "HALFOFF":
        discount = .5
        print("Discount applied")
        break
    else:
        print("Invalid code")
        attempt += 1

# EXERCISE 6 — Print receipt
# Your code here
if not order_descriptions:
    print("\nNo pizzas ordered. See you next time!")
else:
    print("====================================")
    print("     YOUR ORDER RECEIPT")
    print("====================================")
    subtotal = 0
    most_expensive = 0
    for pizza in range(len(order_descriptions)):
        print(f"{pizza + 1}. {order_descriptions[pizza]}")
        print(f"                            ${order_prices[pizza]:>5.2f}")
        subtotal += order_prices[pizza]

    tax = subtotal * .07
    discounted_price = (subtotal + tax) * discount
    total = subtotal + tax - discounted_price
    print("------------------------------------")
    print(f"Subtotal:                   ${subtotal:>5.2f}")
    print(f"Tax (7%):                    ${tax:>4.2f}")
    print(f"Total:                      ${total:>5.2f}")
    print("====================================")
    print("Thank you for your order!")


    # EXERCISE 7 — Find most expensive pizza
    for pizza in range(len(order_descriptions)):
        if order_prices[pizza] > most_expensive:
            most_expensive = order_prices[pizza]

    print(f"Most expensive pizza:       ${most_expensive}")

    # EXERCISE 9 — Count pizzas by size
    personal = 0
    small = 0
    medium = 0
    large = 0
    for size in size_choices:
        if size == 0:
            personal += 1
        elif size == 1:
            small += 1
        elif size == 2:
            medium += 1
        else:
            large += 1
    print(f"Personal: {personal}")
    print(f"Medium: {small}")
    print(f"Large: {medium}")
    print(f"Party: {large}")