# A CorruptedOfficail would take-in certain amount of money
# approve certain documents from the corruptee

# Strategy design aims to refactor out logical steps to an external Interface
# While the "Navigator" class, i.e, the application class, access the method of
#   the Interface to retrieve information/ finish computation

from abc import ABC, abstractmethod

# Define an abstract class that the 'Navigator' depends on
# The ABC should contains all of the required methods that 'Navigator' needs
class BriberyStrategy(ABC):
    def __init__(self, document, valuation, bribery_amount) -> None:
        self.document = document
        self.valuation = valuation
        self.bribery_amount = bribery_amount

    @abstractmethod
    def is_bribery_sufficient(self):
        pass


class LicenseBribery(BriberyStrategy):
    def is_bribery_sufficient(self):
        if self.bribery_amount >= self.valuation * 0.1:
            return self.bribery_amount
        return 0


class PassportBribery(BriberyStrategy):
    def is_bribery_sufficient(self):
        if self.bribery_amount >= self.valuation * 0.3:
            return self.bribery_amount
        return 0


class InformationBribery(BriberyStrategy):
    def is_bribery_sufficient(self):
        if self.bribery_amount >= self.valuation * 0.4:
            return self.bribery_amount
        return 0


## Navigator class 'CorruptedOfficial'
# now acts on the Strategy that is passed into it.
# So rather than having all the information within this class
# those information and logical decisions are refactored into the BriberyStrategy
# and each type of 'Bribery' become a different use-case that have a common
# interface for `CorruptedOfficial` to use on
class CorruptedOfficial:
    income: float = 0

    def process_document(self, document):
        print('=' * 10)
        print(f'Processed Documents - {document}')
        print('=' * 10)

    def accept_bribery(self, amount):
        self.income += amount
        print(f'current income: {self.income}')

    def bribe(self, bribery: BriberyStrategy):

        is_accepted = bribery.is_bribery_sufficient()
        if is_accepted:
            self.process_document(bribery.document)
            self.accept_bribery(bribery.bribery_amount)
            print("Have a nice day.")

        else:
            print("Sorry. Not possible.")


if __name__ == '__main__':
    officer = CorruptedOfficial()

    license_bribery = LicenseBribery('license', 10000, 1000)
    passport_bribery = PassportBribery('passport', 5000, 100)
    officer.bribe(license_bribery)
    officer.bribe(passport_bribery)
