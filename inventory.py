
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.quantity = quantity
        self.cost = cost
        self.product = product
        self.code = code
        self.country = country
    #returns code
    def get_code(self):
        return self.code
    #returns cost as a float
    def get_cost(self):
        return float(self.cost)
    #returns quanitity as float
    def get_quantity(self):
        return float(self.quantity)
    #returns shoe in a readable format
    def __str__(self):
        return f''' -------------------------------------------------------------------------------------------------------------------------------------------
    Model: {self.product} Stock: {self.quantity} Price: {self.cost} Code: {self.code} Country: {self.country}
 -------------------------------------------------------------------------------------------------------------------------------------------
'''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
#list to store shoe objects
shoe_list = []
#==========Functions outside the class==============

#reads data from text file and adds shoe object to list
def read_shoes_data():
    code_list = list(map(lambda x: x.get_code(), shoe_list))
    #try to locate and open inventory file
    try:
        #open inventory data
        with open("inventory.txt", 'r') as inventory:

            #skip over first line with no data
            first_line = inventory.readline()

            #iterate through the remaining lines and extract data from each line
            data = inventory.readlines()
            for entry in data:
                try:
                    info = entry.split(',')
                    country = info[0]
                    codenumber  = info[1]
                    product = info[2]
                    cost = info[3]
                    quantity = info[4]
                    # create new shoe and add new shoe to list
                    #check shoe is not already in list
                    if codenumber not in code_list:
                        shoe = Shoe(country, codenumber, product, cost, quantity)
                        shoe_list.append(shoe)
                except IndexError:
                    print("Some information for this product is missing")

    #if file is missing print error message
    except FileNotFoundError:
        print("Inventory.txt missing!")

#this function allows user to input data and add shoe to list
def capture_shoes():
    country = input("Please enter a country: ")
    product = input("Please enter a product name: ")
    code = (input("Please enter shoe code: "))
    #make sure user enters information in correct format
    while True:
        try:
            cost = input("Please enter cost of shoe: ")
            quantity = input("Please enter quantity of shoe: ")
            break
        #if user enters incorrect number print error message
        except ValueError:
            print("Please enter a number")

    #create new shoe object and add to list
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    try:
        with open("inventory.txt", 'a') as inventory:
            inventory.write("\n" + f"{country},{code},{product},{cost},{quantity}")
    except FileNotFoundError:
        print("File missing")
    print("Shoe successfully added")
    print(len(shoe_list))

#iterate through list and display shoe in readable format
def view_all():
    for shoe in shoe_list:
        print(shoe.__str__())

#show user shoes with lowest stock and allow them to restock
def re_stock():
    #list of all shoe quantities
    quantity_list = list(map(lambda x: x.get_quantity(), shoe_list))
    #find lowest quanitity in list of shoe
    lowest = min(quantity_list)
    #list of shoes with lowest quanitity
    lowest_shoes = []

    print("Items for sale: ")
    #iterate through list of shoes and find shoes with lowest quantity
    for shoe in shoe_list:
        if shoe.get_quantity() == lowest:
            lowest_shoes.append(shoe.product)
            print(shoe.__str__())

    print(lowest_shoes)
    #ask user if they would like to add more stock
    add_stock = input("Do you want to add more stock? 'y' / 'n' : ")
    if add_stock == 'y':
        #failsafe to make sure input is a number
        try:
            number = int(input("Please enter how much stock to add: "))
            try:
                #open text file and find entries with lowest shoes and edit the quanitity
                with open("inventory.txt", 'r') as inventory:
                    #skip first line
                    first_line = inventory.readline()
                    #iterate through lines and edit quantity
                    data = inventory.readlines()
                    for x,entry in enumerate(data):
                        try:
                             info = entry.split(',')
                             if info[2] in lowest_shoes:
                                info[4] = str(number + int(info[4]))  + "\n"
                                data[x] = ','.join(info)
                        except IndexError:
                            print("Some information for this product is missing")

                    #re-write new data to file
                    with open("inventory.txt", 'w') as inventory:
                        inventory.write(first_line)
                        for d in data:
                            inventory.write(d)
            except FileNotFoundError:
                print("Inventory File is missing")
        except ValueError:
            print("Please enter number")




def search_shoe(code):
    #iterate through shoe list and return object with correct code
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
    return None

def value_per_item():
    #iterate through shoe list and calculate value and print answer
    for item in shoe_list:
        value = item.get_cost() * item.get_quantity()
        print(item.__str__() + f''' Value: {value}''')

def highest_qty():
    #map shoe list to list of quantities to find the max
    quantity_list = list(map(lambda x: x.get_quantity(),shoe_list))
    highest = max(quantity_list)
    #iterate through shoe list and display items with lowest quantity
    print("Items for sale: ")
    for shoe in shoe_list:
        if shoe.get_quantity() == highest:
            print(shoe.__str__())

#==========Main Menu=============
read_shoes_data() #initialise shoe_list
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    menu = input('''
Main Menu:
rs - Read All Shoe Data
cs - Capture Shoe 
va - View All Shoe Data
re - Restock shoe
s - Search Shoe
v - Value per item
h - View Highest Shoe Quantity
    ''')
    if menu == 'rs':
        read_shoes_data()
    elif menu == 'cs':
        capture_shoes()
    elif menu == 'va':
        read_shoes_data()
        view_all()
        print(len(shoe_list))
    elif menu == 're':
        re_stock()
    elif menu == 's':
        code = input("Please enter shoe code: ")
        code = code.upper()
        if search_shoe(code) == None:
            print("Invalid code entered")
        else:
            print(search_shoe(code).__str__())
    elif menu == 'v':
        value_per_item()
    elif menu == 'h':
        highest_qty()
    else:
        print("You have made a incorrect choice. Please try again.")