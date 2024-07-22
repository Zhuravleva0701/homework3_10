import threading
from threading import Thread, Lock

lock = Lock()
lock_2 = Lock()


class BankAccount(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 1000


    def deposit(self, amount):
        self.amount = amount
        lock.acquire()
        self.balance += self.amount
        lock.release()
        print(f'Deposit {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        self.amount = amount
        lock_2.acquire()
        self.balance -= self.amount
        lock_2.release()
        print(f'Withdraw {amount}, new balance is {self.balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
