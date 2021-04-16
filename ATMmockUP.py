import random
from datetime import datetime
now = datetime.now()
date = now.strftime("%d %m %y")
time = now.strftime("%X")

"""
    New Customer Registeration Operation
    """
acctDB = {}

def init():

   
    print("Welcome to LizBank")
    print(f"Date:{date}, Time:{time}") 
    print("| 1 | Existing Customer\n| 2 | New Customer\n| 3 | Recover Account Details\n" + "***********" * 2 )
 
    UserInp = int(input("\nSelect Option: "))

    if(UserInp == 1):
        
        login()


    elif(UserInp == 2):
        
        register()


    elif(UserInp == 3):
        recoverDetails()


    else:
        print("You have selected invalid option")
        init()

"""
    Existing Customer Log in Operations
    """
def login():
    allowedUsers = ['000698', '100789']
    allowedPassword = ['1652','2763']
    balanceAmount = 20000.00
    Acct = input("Enter Account Number: ")
    if(Acct in allowedUsers):
        password = input("Enter Pin: ")
        print("*********" * 2)
        userId = allowedUsers.index(Acct)

        if(password == allowedPassword[userId]):

            print("Welcome {}{} {}".format("User, ", "Today is: " + date,time))
            print("Log in successful!")
            print("*********" * 2)
            print('Select an option')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')
            print("*********" * 2)

            selectedOption = int(input('Please select an Option: '))
            print("*********" * 2)


        #Withdrawal
        if(selectedOption == 1):
            print('Withdrawal selected')
            withdrawalAmount = float(input("Enter Amount: "))
            if(withdrawalAmount > balanceAmount):
                print("Insufficient Balance!")
            else:
                print("Take Your Cash: ")
                exit()
             

        #Deposit            
        elif(selectedOption == 2):
            print('Deposit Selected')
            print("*********" * 2)
            depositAmount = float(input("Enter amount: "))
            balanceAmount = balanceAmount + depositAmount
            print(balanceAmount)   

        #Complaint    
        elif(selectedOption == 3):
            complaint=input('What would you like us to do better?')
            print('Thank you for your message, we will get back to you soonest.')   

        else:
            print('Invalid Option selected, please try again')

    else:
        print('Password Incorrect, please try again')
        init()

"""
    New Customer Registeration Operation
    """

def register():

    print("****** Account Opening Page *******")

    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email = input("Enter your email address\n")
    pin = input("create a pin for yourself\n")
    if len(pin) > 4 or len(pin) < 4:
        print("Pin must be 4 numbers")
        register()
    phoneNumber = input("Your Mobile Number\n")
    
    accountNumber = generationAccountNumber()
    acctDB[accountNumber] = [ first_name, last_name, email, pin, phoneNumber]
    acctDB.update({"balance": 1000.0})
    print(acctDB)

    print("Your Account Has been created Successfully!\U0001f500")
    print("***********" * 4)
    print("Your Account Details:")
    print("Account Number:\t %d" % accountNumber)
    print("Full Name:\t \t " + first_name.title() + " " + last_name.title())
    print("Mobile Number:\t " + phoneNumber)
    print("Kindly note that we will send information to your mobile number\n")
    print("***********" * 2)
    print("You have N1000.00 Account Opening Bonus")
    
    print("Thank you for choosing us")
    print("_______________"*2)
    print("\n")
    login()

"""
    Account Recovery Operation
    """ 
def recoveryDetails():
    print("______________"*2 + "\nLost Account Details\n" + "______________"*2)
    print("| 1 | Lost Account Number\n| 2 | Forgot Pin\n| 3 | Change Mobile Number\n" + "***********" * 2)
    UserInp = int(input("\nSelect Option: "))

    if(UserInp == 1):
        print("Kindly call customer care")
        
    elif(UserInp == 2):
        print("Pin recovery Page")
        print("Input your Account Number")
        
    elif(UserInp == 3):
        checker()
                
        
    else:
        print("You have selected invalid option")
        init()

def checker():
    print("Change Mobile Number Page")
    ninCheck = input("Have you registered for NIN? ")
    if ninCheck.lower() == 'yes' or ninCheck.lower() == 'y':
        
        while True:
            UserInp = input("Enter NIN Number: ")
            print("Your NIN: %s \nThank You, we will get back to you!" %UserInp)
            init()
    else:
        print("Wrong input")
        checker()



def logout():
    print("%s, you are logged out!" %acctDB.get("first_name"))
    print("Thank you for Banking with us!")
    login()



init()
