class Budget:

    """
    This is a Budget class

    """
    #Whew! Finally!!!!

    def __init__(self, category, balance):
        self.category = category
        self.balance = balance

    def deposit(self):
        deposit_amount =int(input('Enter amount to deposit: \n'))
        self.balance += deposit_amount
        print(f'Your Balance is {self.balance}')

    def withdrawal(self):
        withdraw_amount = int(input('How much would you like to withdraw? \n'))
        if withdraw_amount > self.balance:
            print('Insufficient Fund!')
        else:
            self.balance -= withdraw_amount
            print(f'Take your cash. Your Balance is {self.balance}')

    def transfer(self, transfer_money):
        print(f'Transfer from {self.category} budget')
        transfer_amount = int(input('Enter amount to transfer: \n'))
        if transfer_amount >= self.balance:
            print('Insufficient Fund!')
        else:
            self.balance -= transfer_amount 
            print(f'Transfer Successful. Your new {self.category} balance is {self.balance}')

    def get_balance(self):
        print(f"{self.category} balance is {self.balance}")
    
def food():
    print('**********FOOD-BUDGET**********')
    foodMain = Budget('food', 20000)
    food_Option = input('''What would you like to do?
    1. deposit
    2. withdraw
    3. transfer
    4. balance \n ''')

    if food_Option == '1':
        foodMain.deposit()

    elif food_Option == '2':
        foodMain.withdrawal()

    elif food_Option== '3':
        transfer = input('''which category would you like to transfer to?
        1.cloth
        2. media \n''')

        if transfer == '1':
            foodMain.transfer('cloth')
        elif transfer == '2':
            foodMain.transfer('media')
        else:
            print('invalid option')
    elif food_Option == '4':
        foodMain.get_balance()
    else:
        print('invalid option selected')
        

def cloth():
    print('*************CLOTH-BUDGET************')
    clothMain = Budget('cloth', 10000)
    cloth_Option = input('''What would you like to do?
    1. deposit
    2. withdraw
    3. transfer
    4. balance \n ''')

    if cloth_Option == '1':
        clothMain.deposit()

    elif cloth_Option == '2':
        clothMain.withdrawal()

    elif cloth_Option== '3':
        transfer = input('''which category would you like to transfer to?
        1.food
        2.media \n''')
        if transfer == '1':
            clothMain.transfer('food')
        elif transfer == '2':
            clothMain.transfer('media')
        else:
            print('Invalid Option')
    elif cloth_Option == '4':
        clothMain.get_balance()
    else:
        print('Invalid Option')
        


def media():
    print('**********MEDIA-BUDGET*********')
    mediaMain = Budget('Media', 15000)
    media_Option= input('''What would you like to do?
    1. deposit
    2. withdraw
    3. transfer
    4. balance \n ''')

    if media_Option == '1':
        mediaMain.deposit()

    elif media_Option == '2':
        mediaMain.withdrawal()

    elif media_Option== '3':
        transfer = input('''which category would you like to transfer to?
        1.food
        2.cloth \n''')
        if transfer == '1':
            mediaMain.transfer('food')

        elif transfer == '2':
            mediaMain.transfer('cloth')
        else:
            print('invalid option')
    elif media_Option == '4':
        mediaMain.balance()
    else:
        print('invalid option selected')        
    

import sys
def welcome():
    try:
        print("********** Welcome to BudgetApp **********")
        select_option = int(input('''Select from the budgets below:
        1. Food
        2. Cloth
        3. Media
        4. Exit
        '''))
        if select_option == 1:
            food()  
        elif select_option == 2:
            cloth()  
        elif select_option == 3:
            media()  
        elif select_option == 4:
            print('Thank you and Goodbye')  
        else:
            print("Invalid input")
    except ValueError:
        print("Start Again")


welcome()
