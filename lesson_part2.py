import pysnooper 

def get_input():
    data = {
        'account_no': {
            'prompt': "Enter the account number: ",
            'item_value': None},
        'balance': {
            'prompt': "Enter account balance: ",
            'item_value': None},
        'customer_credit': {
            'prompt': "Enter the customer credit: ",
            'item_value': None},
        'customer_name': {
            'prompt': "Enter the customer name: ",
            'item_value': None},
    }
    #field is the name of the key (account #, balance), field_data are entire dictionaries and prompt and item value are keys 
    #data.items() converts into a list of tuples that contains the key value pair 
    for field, field_data in data.items():
        field_data['item_value'] = input(field_data['prompt'])

    return data


def validate_account_no(account_number):
    if len(account_number) < 5:
        return False
    return True


def validate_balance(balance):
    if len(balance) < 5:
        return False
    return True


def validate_customer_credit(customer_credit):
    if len(customer_credit) < 5:
        return False
    return True


def validate_customer_name(customer_name):
    if len(customer_name) < 5:
        return False
    return True

#unvalidates account no, returns the account_no dictionary 
#adding a new key to the embedded dictionary called is_valid 
#ammends to the data dictionary is_valid key 

#this is called a decorator with the @ sign. Modifies function 
@pysnooper.snoop()
def validate(unvalidated):
    unvalidated['account_no']['is_valid'] = False
    unvalidated['account_no']['validate'] = validate_account_no
    #creating new key called validate and assigning a value of type function (validate_account_no variable) 
    unvalidated['balance']['is_valid'] = False
    unvalidated['balance']['validate'] = validate_balance
    unvalidated['customer_credit']['is_valid'] = False
    unvalidated['customer_credit']['validate'] = validate_customer_credit
    unvalidated['customer_name']['is_valid'] = False
    unvalidated['customer_name']['validate'] = validate_customer_name
    for field, field_data in unvalidated.items():
        field_data['is_valid'] = \
            field_data['validate'](field_data['item_value'])
            
            #validate key is the variable is the variable with the function in it. Paranthese is the paraneter you are passing to it 
            
            #you cannot have a tuple with 1 value in it, unless you have 

    return unvalidated


def main():
    mydata = get_input()
    my_valid_data = validate(mydata)
    print(my_valid_data)  # just to show


#calling main 
#run main 
if __name__ == "__main__":
    main()