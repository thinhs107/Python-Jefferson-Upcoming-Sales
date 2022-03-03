import csv


def output_to_csv(dataframe):
    filename = '../Upcoming_sale.csv'

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(dataframe)