class Account:
    def __init__(self, name):
        self.__name = name
        self.__balance = 0

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            return False
        self.__balance -= amount
        return True

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name