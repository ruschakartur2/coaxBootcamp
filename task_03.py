import csv

carName = input('Enter the car name')
newCar = {}

with open('items.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        items = {row['name']: {'price': {row['value'], row['currency']}}}
        for name, price in items.items():
            for value, currency in price.values():
                if carName == name:
                    print('You enter', carName, 'price for this car is:', value , currency)
