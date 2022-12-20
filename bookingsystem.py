import string
import datetime

"""# Assignment 7
## Time to complete this assignment:
You have two weeks for this assignment.
## Motivation:
You have been hired to build a booking quote system for transporting packages.
You will write this system in Python, as a terminal application. You will use
simple terminal IO (input and print) as a user interface for now. Another
developer in the future will convert this to a server application that is
front-ended with a browser (you don’t need to worry about how this happens as
it’s not part of your work, but it can and should influence how you build your
system).
The application you are building will capture the following information:

* Name of the customer.
* Package description.
* Are the contents dangerous? [Y/N]
* Weight (kgs).
* Volume (cubic meters).
* Required delivery date (month/date/year).
* International destination? [Y/N]

The application will then attempt to find the best way to route the package (air / ground / ocean).
The rules it will use are as follows:
1. Packages can only be shipped if they weigh less than 10Kg **or** are smaller
than 5x5x5 meters (125 cubic meters).
1. If the package contains dangerous goods it cannot be routed via air.
1. ‘Urgent’ means a package has to be delivered in less than 3 business days.
1. If the package is urgent it will be routed via air, if possible.
1. If the package is heavy or large (towards the maximum end of the boundaries
set in 1 above), and is not urgent, it can be routed via truck (or even ocean
if it is for an international destination).
1. Air shipments cost $10 per kilogram or $20 per cubic meter, whichever is
the highest.
1. Truck shipments cost a flat rate of $25, or $45 if urgent.
1. Ocean shipments costs a flat rate of $30.
Your system will apply these rules to the booking and will calculate
alternative shipping options (or one, or possibly none, depending on how the
above rules affect the booking).
The shipping options must be printed in a clearly understood format, and
should be appended to a booking_quotes.csv file. There will be one row in the
file for each quote.
This application is to be developed using an object oriented approach.
It will require extensive automated tests to ensure the above rules are
correctly applied by the system.
## Here is what you need to do:
1. Use automated testing to validate the system behaves as intended.
1. Develop the data capture functionality, paying careful attention to any
implied data needs.
1. Make sure the data is validated, so data entry errors can be prevented as
much as possible.
1. Build a menu so the system is easy to use.
1. Ensure each booking has a unique id.
1. Make use of formatting techniques to ensure that information reported to
the screen is well laid out and easy to understand.
1. Be sure each booking quote is stored in the csv file.
1. Be sure to commit to local git frequently and use a virtual environment.
## Submission:
Your submission should include the following:
1. All Python (.py) files, including tests, that you developed.
1. The csv file with some quote data in it.
1. Any other files required to run your code.
Your submission **should not** include your virtual environment. To ensure this, create your
virtual environment in the parent folder of your assignment repository.
## Tips
1. Be creative! Use this as an oportunity to reflect on everything you have
learned so far and apply it to application development.
1. Consider making your user interface fully separated from the rest of the project. This will make it
easier to implement a new web-based interface later on without having to modify the underlying implementation."""


""" * Weight (kgs).
* Volume (cubic meters).
* Required delivery date (month/date/year).
* International destination? [Y/N]"""

#why we are putting this into a dictionary? We can put this into a function. 
"""
* Name of the customer.
* Package description.
* Are the contents dangerous? [Y/N]
* Weight (kgs).
* Volume (cubic meters).
* Required delivery date (month/date/year).
* International destination? [Y/N]"""

#def get_transportation_data():
"""def get_transportation_data():
    shipping_open = True 
    while shipping_open:
        transporting_package = {}
        #transporting_package['customer_name'] = input("Please input the customer name ")
        #transporting_package['package_description'] = input("Please enter the package description ")
        #transporting_package['dangerous_contents'] = input('Are the contents dangerous? [Y/N] ')
        transporting_package['weight'] = input('What is the weight of your item ')
        #transporting_package['date'] = input('What is the required delivery date? [DD-MM-YY]')
        #transporting_package['international_delivery'] = input('Is this an international delivery?')
        shipping_open = False"""
    
    

#function should always be named with a verb 
def get_transportation_data():

    transporting_package = {}
    transporting_package['customer_name'] = input("Please input the customer name ")
    transporting_package['package_description'] = input("Please enter the package description ")
    transporting_package['dangerous_contents'] = input('Are the contents dangerous? [Y/N] ')
    while True:
        transporting_package['weight'] = input('What is the weight of your item ')
        if transporting_package['weight'].isnumeric(): #works with strings as well 
            transporting_package['weight'] = int(transporting_package['weight'])
            break
        else:
            print("Please enter a valid number")
            continue
        
    #input functions always return a string 
    
    transporting_package['date'] = input('What is the required delivery date?')
    transporting_package['international_delivery'] = input('Is this an international delivery? [Y/N]' )
    #print(transporting_package['weight'])
    
    return transporting_package
 #putting in the break as soon as it hits a characters thats not a letter it will break out of the loop, otherwise it will keep printing each letter

def validate_transportation_data(transporting_package):
    #testing for it to be invalid 
    if not (5 <= len(transporting_package['customer_name']) <= 15):
            print('Invalid customer name must be between 5 and 15 characters')
    for letter in transporting_package['customer_name']:
        if letter not in string.ascii_letters + " ":
            print('Invalid customer name, customer name must only contain letters')
            break
    if not (10 <= len(transporting_package['package_description']) <= 25):
        print("Package name should be between 10 and 25 characters")
    if not (transporting_package['dangerous_contents'] in "YyNn"):
        print("Dangerous content flag is invalid, must be Y or N")
    if not (1 <= transporting_package['weight'] <= 100): 
        print('Weight must be between a minimum of .5 KG and a maximum of 100 KG')
    date_format = "%m-%d-%y"
    try:
        date_object = datetime.datetime.strptime(transporting_package['date'], date_format)
    except ValueError:
        print("Date format is invalid")
    if not (transporting_package['international_delivery'] in "YyNn"):
        print("International delivery flag is invalid, must be Y or N")


def main(): 
        transporting_package = get_transportation_data()
        transporting_package = validate_transportation_data(transporting_package)

    #print(transporting_package['customer_name'])
    #print(transporting_package['package_description'])
    #print(transporting_package['dangerous_contents'])
    
if __name__ == "__main__":
        main()

#print(get_transportation_data)

#ideally we build it out in components so that errors are being passed after each input 

#add the weight and the volume 
#create validation for those
#critize the code and validation logic 