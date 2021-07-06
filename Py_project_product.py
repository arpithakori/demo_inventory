import csv
import re
import subprocess
import pytest

regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# noinspection RegExpUnexpectedAnchor
rule = re.compile(r'/^[0-9]{10,14}$/')

# Define global variables
product_fields = ['product_id', 'description', 'product_stock','price']
product_database = 'product.csv'

def display_menu():

    print("--------------------------------------")
    print(" Welcome to product Management System")
    print("---------------------------------------")
    print("1. Add New product")
    print("2. View product ")
    print("3. Search product")
    print("4. Update product Details")
    print("5. Delete product Record")
    print("6. Quit")



def add_product():
    print("-------------------------")
    print("Add product Information")
    print("-------------------------")
    global product_fields
    global product_database

    product_data = []
    while True:
        try:
            value = int(input("Enter your product_id: "))
            product_data.append(value)
            break
        except ValueError:
            print("Sorry, Enter valid id.")
            continue

    while True:
        # noinspection PyBroadException
        try:
            description1 = input("Enter description:")
            if description1 != "":
                product_data.append(description1)
                break
        except Exception:
            print("please enter description:")
            continue

    while True:
        try:
            product_stock = int(input("Enter the stock: "))
            product_data.append(product_stock)
            break
        except ValueError:
            print("Sorry, Please enter the stock again.")
            continue

    while True:
        try:
            price = int(input("Enter the price: "))
            product_data.append(price)
            break
        except ValueError:
            print("Sorry, Please enter the price again.")
            continue

    with open(product_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([product_data])
        print("product added Successfully..")
    input("Press any key to continue")
    return

def view_product():
    global product_fields
    global product_database

    print("--- product Records ---")

    with open(product_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in product_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")

def search_product(id):
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


def update_product():
    global product_fields
    global product_database

    print("--- Update product Record ---")
    product_id = input("Enter ID. to update: ")
    index_product = None
    updated_data = []
    with open(product_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if product_id == row[0]:
                    index_product = counter
                    print("product Found: at index ", index_product)
                    product_data = []
                    for field in product_fields:
                        value = input("Enter " + field + ": ")
                        product_data.append(value)
                    updated_data.append(product_data)
                else:
                    updated_data.append(row)
                counter += 1

    # Check if the record is found or not
    if index_product is not None:
        with open(product_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
            print("Data updated..")
    else:
        print("ID. not found in our database")

    input("Press any key to continue")


def delete_product():
    global product_fields
    global product_database

    print("--- Delete product Record ---")
    id_no = input("Enter ID to delete: ")
    product_found = False
    updated_data = []
    with open(product_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if id_no != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    product_found = True

    if product_found is True:
        with open(product_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID", id_no, "deleted successfully")
        print("After deletion the records:")
        with open(product_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for x in product_fields:
                print(x, end='\t |')
            print("\n-----------------------------------------------------------------")

            for row in reader:
                for item in row:
                    print(item, end="\t |")
                print("\n")

    else:
        print("ID not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_product()
    elif choice == '2':
        view_product()
    elif choice == '3':
        print("--- Search product Record ---")
        id_no = input("Enter ID. to search: ")
        search_product(id_no)
    elif choice == '4':
        update_product()
    elif choice == '5':
        delete_product()
    elif choice == '6':
        subprocess.call(" py_user.py ", shell=True)


print("-------------------------------")
print("            Thank you          ")
print("-------------------------------")
