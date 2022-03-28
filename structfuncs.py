def user_details_before(bank_obj, id: int):
    print('\nUpdating')
    bank_obj.display_information(unique_id = id)
    

def user_details_after(bank_obj, id: int):
    print('\nUpdates were applied successfully')
    bank_obj.display_information(unique_id = id)

def display_options_1():
    print('1. Display information\n2. Add new customer\n3. Remove customer\n4. Update customer details\n5. Search details about customer\n0. Exit')

def add_customer(bank_obj, main):
    try:
        
        first_name = input('First name: ').capitalize()
        last_name = input('Last name: ').capitalize()
        age = int(input('Age: '))
        id = int(input('ID: '))
        bank_obj.add_new_customer(first_name, last_name, age, id)
        
        print(f'Customer {first_name} {last_name} was added successfully')
        main()
    except ValueError:
        print('Invalid Values')

    except KeyboardInterrupt:
        main()
            
def delete(bank_obj, main):
        try:
            enter_id = int(input('ID: '))
            bank_obj.delete_customer(unique_id = enter_id)
            print(f'Deleted customer with id: {enter_id} was deleted successfully')
        except ValueError:
            print('Invalid value')
            delete(bank_obj, main)
        except KeyboardInterrupt:
            main()
                                
def update_details(bank_obj, main): # Devide functions inside functions to clear code (maybe decorator later)
    
    def first_name_update():
        enter_user_id = int(input('ID: '))
        bank_obj.display_information(unique_id = enter_user_id)
        
        enter_first_name = input('First name: ').capitalize()
        bank_obj.update_customer_first_name(enter_first_name, enter_user_id)
        bank_obj.display_information(unique_id = enter_user_id)

    
    def last_name_update():
        enter_user_id = int(input('ID: '))
        bank_obj.display_information(unique_id = enter_user_id)
                        
        enter_last_name = input('Last name: ').capitalize()
        bank_obj.update_customer_last_name(enter_last_name, enter_user_id)
        bank_obj.display_information(unique_id = enter_user_id)
        
    def age_update():
        enter_user_id = int(input('ID: '))
        bank_obj.display_information(unique_id = enter_user_id)
        
        enter_age = int(input('Age: '))
        bank_obj.update_customer_age(enter_age, enter_user_id)
        bank_obj.display_information(unique_id = enter_user_id)

        
    def all_update():
        enter_user_id = int(input('ID: '))
        bank_obj.display_information(unique_id = enter_user_id)
        
        enter_first_name = input('First name: ').capitalize()
        enter_last_name = input('Last name: ').capitalize()
        enter_age = int(input('Age: '))        
        
        bank_obj.update_customer_all_information(enter_first_name, enter_last_name, enter_age, enter_user_id)
        bank_obj.display_information(unique_id = enter_user_id)
     
     
    while True:
        print('1. Update first name\n2. Update last name\n3. Update age\n4. Update all\n0. Back')
        enter_choice = input('>>>')
        
        if enter_choice == '0':
            main()
            
        elif enter_choice == '1':
            first_name_update()
        
        elif enter_choice == '2':
            last_name_update()
            
        elif enter_choice == '3':
            age_update()
            
        elif enter_choice == '4':
            all_update()

def search_customer(bank_obj):
    enter_user_id = int(input('ID: '))
    bank_obj.display_information(unique_id = enter_user_id)    
    print('')
