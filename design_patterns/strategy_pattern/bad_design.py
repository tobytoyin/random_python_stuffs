# A CorruptedOfficail would take-in certain amount of money
# approve certain documents from the corruptee
class CorruptedOfficial:
    income: float = 0

    def check_bribery_amount(
        self,
        document_type,
        document_valuation,
        bribery_amount,
    ) -> bool:
        if document_type == 'license':
            acceptable_rate = 0.1

        elif document_type == 'passport':
            acceptable_rate = 0.3

        elif document_type == 'information':
            acceptable_rate = 0.4

        else:
            acceptable_rate = 0.05

        if bribery_amount >= document_valuation * acceptable_rate:
            return bribery_amount

        return 0

    def process_document(self, document):
        print('=' * 10)
        print(f'Processed Documents - {document}')
        print('=' * 10)

    def accept_bribery(self, amount):
        self.income += amount
        print(f'current income: {self.income}')

    def bribe(
        self,
        document_type,
        document_valuation,
        bribery_amount,
    ):

        is_accepted = self.check_bribery_amount(document_type, document_valuation, bribery_amount)
        if is_accepted:
            self.process_document(document_type)
            self.accept_bribery(bribery_amount)
            print("Have a nice day.")

        else:
            print("Sorry. Not possible.")


if __name__ == '__main__':
    officer = CorruptedOfficial()
    officer.bribe('license', 10000, 1000)
    officer.bribe('passport', 5000, 100)
