print('hello, welcome to potato cafe!!!')
#welcomes the customer

name = input('whats your name? ')
#defines variable name as what costumer types

if name == 'ben' or name == 'patricia' or name == 'loki':
    evil_status = input('are you evil?')
    good_deeds = int(input('How many good deeds did you do today?'))
    if evil_status == 'yes' and good_deeds < 4:
        print('GET OUT OF HERE, {}'.format(name.upper()))
#if the costumer types ben, patricia or loki, the system will ask if
#is evil, if you answer with yes then it will ask how manny good
#deeds did you do that day, if the answer is less than 4 it will kick
#the costumer out..

    else:
        print(f'Welcome {name}!! Is a great day today isnt it?\n')
        menu = ['cappuccino', 'chocolate', 'milk', 'latte', 'frappucino']
# if the person answers that they are not evil they will be welcome in
#to the shop


        print(f'Here is your menu, {name}.\n\n{menu}\n')
#it will give the costumer the menu

        order = input('May I have your order, please? ')
#it will ask for the costumers oder

        price = 0
        if order == 'latte':
            whipped_cream = input('do you want whipped cream?')
            if whipped_cream == 'yes':
                price = 11
            else:
                price = 5
# if the costumer aks for latte it will ask if he wants whipped cream
# and if he wants it he will need to pay 11 dollars instead of 5

        elif order == 'milk':
            price = 6
# if costumer orders milk, price will be defined to 6

        elif order == 'cappuccino' or 'chocolate':
            price = 7
#if costumer asks for cappuccino or chocolate price will be defined
#to 7

        elif order == 'frappuccino':
            price = 8
#if costumer orders frappuccino price will be defined to 8

        if order not in menu:
            print('Sorry, we dont have that here')
            exit()
#if the costumer orders something that isn't on the menu it will say
#that the system doesnt have it and it will exit the code

        quantity = int(input('how manny coffees would you like??'))
        total = quantity * price
#here it will ask for the quantity of the order, and then calculate 
#the price by multiplying the quantity for the price of 1 order

        print(
            f"sounds good {name}, we'll have your {quantity} {order}s in a moment.")
        print('Your total will be {}€ .'.format(total))
#says the total price of the order

elif name != 'ben' or 'patricia' or 'loki':
    print(f'Welcome {name}!! Is a great day today isnt it?\n')
    menu = ['cappuccino', 'chocolate', 'milk', 'latte', 'frappuccino']
#if name is diferent to 'ben', 'patricia' and 'loki' it will greet
#them as normal

    print(f'Here is your menu, {name}.\n{menu}\n')
#it will give the costumer the menu

    order = input('May I have your order, please? ')
#it will ask for the costumers oder

    price = 0
    if order == 'latte':
            whipped_cream = input('do you want whipped cream?')
            if whipped_cream == 'yes':
                price = 11
            else:
                price = 5
# if the costumer aks for latte it will ask if he wants whipped cream
# and if he wants it he will need to pay 11 dollars instead of 5

    elif order == 'milk':
            price = 6
# if costumer orders milk, price will be defined to 6

    elif order == 'cappuccino' or 'chocolate':
            price = 7
#if costumer asks for cappuccino or chocolate price will be defined
#to 7

    elif order == 'frappuccino':
            price = 8
#if costumer orders frappuccino price will be defined to 8

    if order not in menu:
            print('Sorry, we dont have that here')
            exit()
#if the costumer orders something that isn't on the menu it will say
#that the system doesnt have it and it will exit the code

    quantity = int(input('how manny coffees would you like??'))
    total = quantity * price
#here it will ask for the quantity of the order, and then calculate 
#the price by multiplying the quantity for the price of 1 order

    print(
            f"sounds good {name}, we'll have your {quantity} {order}s in a moment.")
    print('Your total will be {}€ .'.format(total))
#says the total price of the order
