import csv

#Remove rows that aren't Pink Morsels
#Remove quantity and price fields, replace with net 'sales' field
files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv',]
field_names = ['sales', 'date', 'region']

writer = csv.DictWriter(open('data/pinkMorselSales.csv', 'w', newline=''), fieldnames=field_names)
writer.writeheader()

for file in files:
    with open(file) as dataset:
        csv_reader = csv.DictReader(dataset, delimiter=',') #Delimiter separates columns
        for row in csv_reader:
            if row['product'] == 'pink morsel':
                writer.writerow({
                    'sales': "$" + "{:.2f}".format(int(row['price'].replace("$","").replace(".","")) * int(row['quantity']) / 100.0),
                    'date': row['date'],
                    'region': row['region']
                })
            
