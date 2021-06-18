from Debitcard import Debitcard

# Client
class You:
    def __init__(self):
        print("You:: Lets buy a denim shirt!")
        self.debitCard = Debitcard()    #
        self.isPurchased = None         # bool type

    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You:: Purchased denim shirt")
        else:
            print("You:: No Money")