import sqlite3

class BankStructure:
    
    def __init__(self, bank_name: str = 'Chinchlavs bank', database_name: str = 'customers.db', table_name: str = 'bankcustomers'):
        self.bank_name = bank_name
        self.database_name = database_name
        self.table_name = table_name
        
        self.conn = sqlite3.connect(self.database_name)
        self.cur = self.conn.cursor()
        self.__create_table()
        
    def __loop_fetch(self, cursor):
        for i in cursor.fetchall():
                print(i)
    
    def __create_table(self): # ყველა ინიციალიზაციაში გასაშვებათ, რათა დავრწმუნდეთ, რომ მაგიდა ყოველთვის არსებობს და არ აერორებს
        self.cur.execute(f'''
                            CREATE TABLE IF NOT EXISTS {self.table_name} (
                                first_name CHAR(50),
                                last_name CHAR(50),
                                age INT,
                                id INT UNIQUE NOT NULL
                                )''')
    # Display
    def display_information(self, all: bool = None, unique_id: int = None):
        if all is not None and unique_id is None:
            self.cur.execute(f'SELECT rowid, * FROM {self.table_name}')
            self.__loop_fetch(self.cur)

        elif unique_id is not None and all is None:
            self.cur.execute(f'SELECT rowid, * FROM {self.table_name} WHERE id = {unique_id}')
            self.__loop_fetch(self.cur)
            
    # Add customer
    def add_new_customer(self, first_name: str, last_name: str, age: int, id: int): # Adds new customer and checks for unique value exception
        try:
            self.cur.execute(f'''
                            INSERT INTO {self.table_name}(first_name, last_name, age, id) VALUES("{first_name}", "{last_name}", {age}, {id})
                            ''')
            self.conn.commit()
        except sqlite3.IntegrityError:
            print('User with the given ID already exists')
    
    # Delete customer
    def delete_customer(self, unique_id: int): # Deletes customer by unique id
        self.cur.execute(f'DELETE FROM {self.table_name} WHERE id = {unique_id}')
        self.conn.commit()
        
    # Update methods    
    def update_customer_all_information(self, first_name: str, last_name: str, age: int, unique_id: int): # Updates all information by unique id
        self.cur.execute(f'''
                        UPDATE {self.table_name} SET
                        first_name = "{first_name}",
                        last_name = "{last_name}",
                        age = {age}
                        WHERE id = {unique_id}
                        ''')
        self.conn.commit()
     
    def update_customer_first_name(self, first_name: str, unique_id: int):
        self.cur.execute(f'UPDATE {self.table_name} SET first_name = "{first_name}" WHERE id = {unique_id}')
        self.conn.commit()
            
    
    def update_customer_last_name(self, last_name: str, unique_id: int):
        self.cur.execute(f'UPDATE {self.table_name} SET last_name = "{last_name}" WHERE id = {unique_id}')
        self.conn.commit()
    
    def update_customer_age(self, age: int, unique_id: int):
        self.cur.execute(f'UPDATE {self.table_name} SET age = {age} WHERE id = {unique_id}')
        self.conn.commit()

bank = BankStructure()

