import csv
import re
import subprocess
import pytest

product_fields = ['product_id', 'description', 'product_stock','price']
product_database = 'product.csv'

def search(id):
    global product_database
    global product_fields

    foundFlag = 0
    #print("--- Search product Record ---")
    #id_no = input("Enter ID. to search: ")
    id_no = id
    with open(product_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if id_no == row[0]:
                    foundFlag = 1
                    print("----- product Found -----")
                    print("ID: ", row[0])
                    print("Description: ", row[1])
                    print("product_Stock: ", row[2])
                    print("price: ", row[3])
                    break
        else:
            print("ID. not found in our database")
    print(foundFlag)
    return foundFlag
    input("Press any key to continue")

