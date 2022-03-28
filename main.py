from structure import *
from structfuncs import *

def main():
    bank = BankStructure()
    print(f'Welcome to "{bank.bank_name}"\nChoose an operation you would like to use\n')
    
    while True:
        display_options_1()
        try:
            enter = input('>>>')
        except KeyboardInterrupt:
            bank.conn.close()
            quit()
        if enter == '0':
            bank.conn.close()
            quit()
        elif enter == '1':
            bank.display_information(all=True)
        elif enter == '2':
            add_customer(bank, main)
        elif enter == '3':
            delete(bank, main)
        elif enter == '4':
            update_details(bank, main)
        elif enter == '5':
            search_customer(bank)
main()

