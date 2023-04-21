class Account:
    """
    This class represents the bank account
    name : str
        name of the account person
    balance : float
        current balance of account
    """

    def __init__(self, name: str) -> None:
        """
        Starts the Account class.

        Defaults name and balance
        """
        self.__name = name
        self.__balance = 0.0

    def deposit(self, amount: float) -> bool:
        """
        Deposits the specified amount to account

        amount : float
            Amount to be deposited.

        Returns:
        bool
            True if deposit successful, False otherwise
        """
        if amount <= 0:
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws amount from account.

        Parameters:
        amount : float
            Amount to withdraw.

        Returns:
        bool
            True if withdrawal successful, False otherwise.
        """
        if amount <= 0 or amount > self.__balance:
            return False
        self.__balance -= amount
        return True
    def get_name(self) -> str:
        """
        Return name.
        Returns:
            str: Name of object.
        """
        return self.__name

