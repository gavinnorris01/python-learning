#Problem 1
amount = float(input("Enter amount: "))
currency = input("Enter currency (USD/EUR/GBP): ").upper()

if (currency == "USD"):
    conv1 = amount * .92
    conv2 = amount * .79
    print(f"{amount} USD = {conv1:f} EUR")
    print(f"{amount} USD = {conv2:f} GBP")

elif (currency == "EUR"):
    conv1 = amount * 1.09
    conv2 = amount * .86
    print(f"{amount} EUR = {conv1:f} USD")
    print(f"{amount} EUR = {conv2:f} GBP")

elif (currency == "GBP"):
    conv1 = amount * 1.27
    conv2 = amount * 1.16
    print(f"{amount} GBP = {conv1:f} USD")
    print(f"{amount} GBP = {conv2:f} EUR")

else:
    print("Invalid currency")
    
#Problem 2

email = input("Enter an email address: ")
fails = 0
atCount = 0

for char in email:
    if (char == "@"):
        atCount += 1

if (atCount == 1):
    single = "Pass"
    
else:
    single = "Fail"
    fails += 1

if (email.index("@") <= 0):
    textBefore = "Fail"
    fails += 1
    
else:
    textBefore = "Pass"

if ("." in email):
    if (email.index(".") >= email.index("@")):
        dot = "Pass"

    else:
        dot = "Fail"
        fails += 1

    if (email.index(".") <= len(email) - 2):
        domain = "Pass"

    else:
        domain = "Fail"
        fails += 1

else:
    fails += 2
    dot = "Fail"
    domain = "Fail"

totalFails = fails
space = "Pass"

for char in email:
    if (char == " "):
        space = "Fail"
        totalFails += 1

print(f"Single @: {single}")
print(f"Text before @: {textBefore}")
print(f"Dot after @: {dot}")
print(f"Domain extention: {domain}")
print(f"No spaces: {space}")

if (totalFails == 0):
    print("Criteria met: 5/5")
    print("Result: Valid email address")

elif (totalFails <= 2):
    print(f"Criteria met: {totalFails}/5")
    print("Result: Possibly valid -- review format")

else:
    print(f"Criteria met: {totalFails}/5")
    print("Result: Invalid email address")
    

#Problem 4

age = int(input("What is your age: "))
matinee = (input("Is the movie matinee or evening: ").upper())
rewards = bool(input("Are you a rewards member: "))

if (matinee == ("MATINEE" or "EVENING")):
    matineePrice = 2.00

    if (age < 12):
        price = 6.00

    elif (age < 18):
        price = 9.00

    elif (age < 65):
        price = 13.00
    
    else:
        price = 7.00
    
    if (rewards == True):
        rewardsDiscount = (price - matineePrice) * .15
        finalPrice =  price - rewardsDiscount - matineePrice
        
    else:
        finalPrice = price - matineePrice
        
    print("Movie Ticket")
    print(f"Age: {age}")
    print("Showtime: Matinee")
    print(f"Rewards Member: {rewards}")
    print(f"Base Price: {price}")
    print(f"Matinee Discount: -{matineePrice}")
    print(f"Rewards Discount: -{rewardsDiscount}")
    print(f"Final Price: {finalPrice}")
    
else:
    print("Invalid showtime")
    

