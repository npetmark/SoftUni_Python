# Input
fruit = input()
day = input()
quantity = float(input())

# Logic
price = 0

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = 2.5

    elif fruit == 'apple':
        price = 1.2

    elif fruit == 'orange':
        price = 0.85

    elif fruit == 'grapefruit':
        price = 1.45

    elif fruit == 'kiwi':
        price = 2.7

    elif fruit == 'pineapple':
        price = 5.5

    elif fruit == 'grapes':
        price = 3.85

elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = 2.7

    elif fruit == 'apple':
        price = 1.25

    elif fruit == 'orange':
        price = 0.9

    elif fruit == 'grapefruit':
        price = 1.60

    elif fruit == 'kiwi':
        price = 3.0

    elif fruit == 'pineapple':
        price = 5.6

    elif fruit == 'grapes':
        price = 4.2

if price == 0:
    print('error')
else:
    price *= quantity
    print(f'{price:.2f}')
