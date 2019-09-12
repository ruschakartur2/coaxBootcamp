import csv

while True:
    car_name = input('Enter the car name')
    new_cars = {}
    EUR = 0.90
    GBP = 0.81

    with open('items.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        cars = {row['name']: {'price': row['value']} for row in reader}

    if car_name in cars:
        value = cars[car_name]['price']
        print(f'You enter: {car_name} price for this car is: {value} $')
    else:
        currency, value = input('Pls add currency type and value: ').split()
        try:
            value = float(value)
            if currency == 'EUR':
                value *= EUR
            elif currency == 'GBP':
                value *= GBP
            new_cars[car_name] = {'price': value}
        except ValueError:
            print('Error.Please enter number!')
        else:
            pass
    if new_cars:
        with open('items.csv','a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name', 'value'])
            writer.writerow({'name': car_name,'value' : value})