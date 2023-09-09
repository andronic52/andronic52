print('hello, welcome to potato cafe!!!')

name = input('whats your name? ')

if name == 'ben' or name == 'patricia' or name == 'loki':
    evil_status = input('are you evil?')
    good_deeds = int(input('How many good deeds did you do today?'))
    if evil_status == 'yes' and good_deeds < 4:
        print('GET OUT OF HERE, {}'.format(name.upper()))

    else:
        print(f'Welcome {name}!! Is a great day today isnt it?\n')
        menu = ['cappuccino', 'chocolate', 'milk', 'latte', 'frappucino']

        print(f'Here is your menu, {name}.\n\n{menu}\n')
        order = input('May I have your order, please? ')
        price = 0
        if order == 'latte':
            whipped_cream = input('do you want whipped cream?')
            if whipped_cream == 'yes':
                price = 11
            else:
                price = 5
        elif order == 'milk':
            price = 6
        elif order == 'cappuccino' or 'chocolate':
            price = 7
        elif order == 'frappuccino':
            price = 8
        if order not in menu:
            print('Sorry, we dont have that here')
            exit()

        quantity = int(input('how manny coffees would you like??'))
        total = quantity * price

        print(
            f"sounds good {name}, we'll have your {quantity} {order}s in a moment.")
        print('Your total will be {}€ .'.format(total))
elif name != 'ben' or 'patricia' or 'loki':
    print(f'Welcome {name}!! Is a great day today isnt it?\n')
    menu = ['cappuccino', 'chocolate', 'milk', 'latte', 'frappuccino']

    print(f'here is your menu, {name}\n\n{menu}\n')
    order = input('May I have your order, please? ')
    price = 0
    if order == 'latte':
        whipped_cream = input('do you want whipped cream?')
        if whipped_cream == 'yes':
            price = 11
        else:
            price = 5
    elif order == 'milk':
        price = 6
    elif order == 'cappuccino' or 'chocolate':
        price = 7
    elif order == 'frappuccino':
        price = 8
    if order not in menu:
        print('Sorry, we dont have that here')
        exit()

    quantity = int(input('how manny coffees would you like??'))
    total = quantity * price

    print(
        f"sounds good {name}, we'll have your {quantity} {order}s in a moment.")
    print(f'Your total will be {total}€ .')
