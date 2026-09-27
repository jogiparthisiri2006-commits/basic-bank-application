class Account:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if amount<=0:
            print("Invalid amount")
        elif amount<=self.__balance:
             self.__balance-=amount
             print(f"{amount} withdraw successfully")
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
    def display_details(self):
        print("\n------Account Details------")
        print("Holder_name:",self.name)
        print("Balance:",self.get_balance())
account=Account("Siri",50000)
account.display_details()
account.deposit(2000)
account.withdraw(5000)
account.display_details()
