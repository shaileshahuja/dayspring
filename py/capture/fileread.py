import csv


def read():
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print row

