class BankAccount:
    def __init__(self, starting_balance):
        self.balance = starting_balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.balance}")
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.balance}")
        else:
            print("Insufficient funds!")
simon_account =BankAccount(100)
simon_account.deposit(50)
simon_account.withdraw(50)




