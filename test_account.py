import pytest
from account import Account

def test_init():
    account = Account("John")
    assert account.name == "John"
    assert account.balance == 0

def test_deposit():
    account = Account("John")
    assert account.deposit(100) == True
    assert account.balance == 100
    assert account.deposit(-50) == False
    assert account.balance == 100

def test_withdraw():
    account = Account("John")
    account.deposit(100)
    assert account.withdraw(50) == True
    assert account.balance == 50
    assert account.withdraw(200) == False
    assert account.balance == 50
    assert account.withdraw(-10) == False
    assert account.balance == 50

def test_get_balance():
    account = Account("John")
    assert account.get_balance() == 0
    account.deposit(100)
    assert account.get_balance() == 100

def test_get_name():
    account = Account("John")
    assert account.get_name() == "John"