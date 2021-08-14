class Atm():
    def __init__(self, cardNumber, pin, balance):
        self.cardNumber = cardNumber
        self.pin = pin
        self.balance = balance

    def checkBalance(self, balance):
        return str(self.balance)
    def deposit(self, balance):
        depositAmount = input("How much would you like to deposit? : ")
        self.balance = self.balance+deposit
        checkBalance()
    def withdraw(self, balance):
        withdrawAmount = input("How much would you like to withdraw? : ")
        self.balance = self.balance+withdraw
        checkBalance()

def main():
    user = Atm(input("Enter you card number: "), input("Enter your pin: "), input("Enter your balance: "))
    userBalance = input("Enter your balance: ")
    answer = input("Would you like to check your balance, withdraw or deposit: ")
    if answer=="deposit":
        userBalance.deposit(balance)
    elif answer=="withdraw":
        userBalance.withdraw(balance)   
    elif answer== "check balance" or answer== "Check Balance":
        print(checkBalance())

if __name__ == "__main__":
    main()
    
