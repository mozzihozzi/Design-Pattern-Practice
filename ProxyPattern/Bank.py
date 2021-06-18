from abc import ABCMeta, abstractmethod


# Subject
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


# RealSubject
class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card    # 가정) 카드번호 == 계좌번호
        return self.account

    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough money")
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False

