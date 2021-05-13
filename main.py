import csv

import pandas as pd

file = "database.csv"


def menu():
    print('''
    --------- MAIN MENU ----------
    (1) Add an Item
    (2) Remove an Item
    (3) Modify an item
    (4) Search (or query) an Item
    (5) Print current inventory
    (6) Exit
    ''')
    # print menu

    print('Enter a choice from the menu above: ')
    choice = input()
    # provide choice input
    switch(choice)


def switch(choice):
    if choice == '1':
        print('Enter the Product ID:')
        PRODUCT_ID = input()
        print('Enter the Product Name:')
        PRODUCT_NAME = input()
        print('Enter the Quantity:')
        QUANTITY = input()
        print('Enter the Price:')
        PRICE = input()
        add_an_item(PRODUCT_ID, PRODUCT_NAME, QUANTITY, PRICE)
    elif choice == '2':
        print('Enter the Product ID:')
        PRODUCT_ID = input()
        remove_an_item(PRODUCT_ID)
        # remove an item
    elif choice == '3':
        print('Enter the Product ID:')
        PRODUCT_ID = input()
        modify_an_item(PRODUCT_ID)
        # modify an item
    elif choice == '4':
        print('Enter the Product ID:')
        PRODUCT_ID = input()
        search(PRODUCT_ID)
        #search
    elif choice == '5':
        print_inventory()
    elif choice == '6':
        print("Exiting Console")
        quit()
    else:
        print("Invalid Entry, try again. ")
        menu()


def add_an_item(PRODUCT_ID, PRODUCT_NAME, QUANTITY, PRICE):
    # define variables
    text = (PRODUCT_ID, ',', PRODUCT_NAME, ',', QUANTITY, ',', PRICE)

    # Open a file with access mode 'a'
    my_file = open(file, 'a')
    # Append 'hello' at the end of file
    my_file.write('\n')
    my_file.write(convert_tuple(text))
    # Close the file
    my_file.close()

    menu()


def remove_an_item(PRODUCT_ID):
    lines = list()
    with open(file, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == PRODUCT_ID:
                    lines.remove(row)
    readFile.close()

    with open(file, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    writeFile.close()


def modify_an_item(PRODUCT_ID):
    df = pd.read_csv(file)
    df.query('PRODUCT_ID == ' + PRODUCT_ID, inplace=True)
    print('''
    --------- MODIFY MENU ----------
    (1) Change a Product ID
    (2) Change a Product Name
    (3) Adjust a Quantity
    (4) Adjust a Price
    (5) Return to Main Menu
    ''')
    print(df)
    print('Enter a choice from the menu above: ')
    choice3 = input()
    modify_menu(choice3,PRODUCT_ID)


def modify_menu(choice3,PRODUCT_ID):
    df = pd.read_csv(file)
    df.query('PRODUCT_ID == ' + PRODUCT_ID, inplace=True)
    if choice3 == '1':
        index_id = 0
        for index in df.index:
            index_id += index
        print('Enter a new Product ID: ')
        New_ID = input()

        New_ID = str(New_ID)
        Name = str(df.loc[index_id, " PRODUCT_NAME"])
        Quantity = str(df.loc[index_id, " QUANTITY"])
        Price = str(df.loc[index_id, " PRICE"])

        remove_an_item(PRODUCT_ID)

        add_an_item(New_ID, Name, Quantity, Price)
    elif choice3 == '2':
        index_id = 0
        for index in df.index:
            index_id += index
        print('Enter a new Product Name: ')
        New_Name = input()

        PRODUCT_ID_NUMBER = str(PRODUCT_ID)
        Quantity = str(df.loc[index_id, " QUANTITY"])
        New_Name = str(New_Name)
        Price = str(df.loc[index_id, " PRICE"])

        remove_an_item(PRODUCT_ID)

        add_an_item(PRODUCT_ID_NUMBER, New_Name, Quantity, Price)
        menu()
    elif choice3 == '3':
        index_id = 0
        for index in df.index:
            index_id += index
        print('Enter a new Quantity: ')
        New_Quantity = input()

        PRODUCT_ID_Number = str(PRODUCT_ID)
        Name = str(df.loc[index_id, " PRODUCT_NAME"])
        New_Quantity = str(New_Quantity)
        Price = str(df.loc[index_id, " PRICE"])

        remove_an_item(PRODUCT_ID)

        add_an_item(PRODUCT_ID_Number, Name, New_Quantity, Price)
        menu()
    elif choice3 == '4':
        index_id = 0
        for index in df.index:
            index_id += index
        print('Enter a new Price: ')
        New_Price = input()

        PRODUCT_ID_Number = str(PRODUCT_ID)
        Name = str(df.loc[index_id, " PRODUCT_NAME"])
        Quantity = str(df.loc[index_id, " QUANTITY"])
        New_Price = str(New_Price)

        remove_an_item(PRODUCT_ID)

        add_an_item(PRODUCT_ID_Number, Name, Quantity, New_Price)
        menu()
    elif choice3 == '5':
        menu()
    else:
        print("Invalid Entry Please try again...")
        modify_an_item(PRODUCT_ID)


def search(PRODUCT_ID):
    data = pd.read_csv(file)
    data.query('PRODUCT_ID == ' + PRODUCT_ID, inplace=True)
    print(data)
    menu()


def convert_tuple(my_tuple):
    string = ''.join(my_tuple)
    return string


def print_inventory():
    print('''
       --------- Sorting Menu ----------
       (1) Alphabetical Order
       (2) Numerical Order of ID#
       (3) Price
       (4) Quantity
       (5) As Is in CSV
       (6) Back to Menu
       ''')

    print("How would you like to sort the inventory?")
    choice2 = input()
    inventory_sort(choice2)


def inventory_sort(choice2):
    data = pd.read_csv(file)
    if choice2 == '1':
        sorted_csv = data.sort_values(by=[' PRODUCT_NAME'])
        print(sorted_csv)
        menu()
    elif choice2 == '2':
        sorted_csv = data.sort_values(by=['PRODUCT_ID'])
        print(sorted_csv)
        menu()
    elif choice2 == '3':
        print('''
        Would you like to print the prices:
        (1) Highest to Lowest
        (2) Lowest to Highest
        ''')
        choice_order = input()
        if choice_order == '1':
            sorted_csv = data.sort_values(by=[' PRICE'], ascending=False)
            print(sorted_csv)
            menu()
        elif choice_order == '2':
            sorted_csv = data.sort_values(by=[' PRICE'], ascending=True)
            print(sorted_csv)
            menu()
        else:
            print("Invalid Entry, Back to Sorting Menu...")
            print_inventory()
    elif choice2 == '4':
        print('''
        Would you like to print the quantity:
        (1) Highest to Lowest
        (2) Lowest to Highest
        ''')
        choice_order = input()
        if choice_order == '1':
            sorted_csv = data.sort_values(by=[' QUANTITY'], ascending=False)
            print(sorted_csv)
            menu()
        elif choice_order == '2':
            sorted_csv = data.sort_values(by=[' QUANTITY'], ascending=True)
            print(sorted_csv)
            menu()
        else:
            print("Invalid Entry, Back to Sorting Menu...")
            print_inventory()
    elif choice2 == '5':
        print(data)
        menu()
    elif choice2 == '6':
        print("Back to Main Menu...")
        menu()
    else:
        print("Invalid Entry, Back to Sorting Menu...")
        print_inventory()


menu()

