from datetime import datetime
now = datetime.now()
date = now.strftime("%d %m %y")
time = now.strftime("%X")

print(f"Date:{date}, Time:{time}")


name = input("Enter name \n")
allowedUsers = ["Liz",'Alex','Fred']
allowedPassword = ['PasswordLiz','passwordAlex','passwordFred']
availableBalance = ['50000','30000','70000']


if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)
    
    if (password == allowedPassword[userId]):
        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))

    
        if(selectedOption == 1):
            withdrawal=input('How much would you like to withdraw?')
            if(withdrawal < availableBalance[userId]):
                print('Please take your cash. Cash retract not available.')
            else:
                print("Insufficient balance")
            
        elif(selectedOption == 2):
            deposit = int(input("How much would you like to deposit? \n"))
            currentBalance=(deposit + int(availableBalance[userId]))
            print('Your Current Balance is', currentBalance)
            
        elif(selectedOption == 3):
            complaint=input('What would you like us to do better on?')
            print('Thank you for contacting us, we will get back to you soonest.')
            
        else:
              print('Invalid Option selected, please try again')

    else:
        print('Password Incorrect, please try again')

else:
    print('Name not found, please try again')
