def open_account():
    print("New account is opened")

def deposit(balance, money):
    print("Deposit is OK. Balance is {0} ".format(balance+money))
    return balance + money

def withdraw(balance,money):
    if balance >= money:
        print("Withdraw is OK. balace is {0}".format(balance - money))
        return balance - money
    else:
        print("Withdraw is can't be done. balance is {0}".format(balance))
        return balance

def withdraw_night(balance,money):
    commission = 100
    return commission, balance - money - commission
    

open_account()

balance = 0
balance = deposit(balance,1000)
print(balance)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 500)
print("Commission is {0}, balance is {1} ".format(commission, balance ))