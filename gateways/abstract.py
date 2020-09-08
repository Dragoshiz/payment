import random


class AbstractPaymentGateway(object):
    def is_available(self):
        raise NotImplementedError

    def process(self, transaction):
        raise NotImplementedError

    def can_process_transaction(self, transaction):
        raise NotImplementedError

    def process_with_retries(self, transaction, retry_count):
        for retry in range(retry_count):
            is_processing = self.is_available()
            if is_processing:
                self.process(transaction)
                break


class ExpensivePaymentGateway(AbstractPaymentGateway):
    def is_available(self):
        randint = random.randint(1, 10)
        return randint > 5

    def can_process_transaction(self, transaction):
        if transaction.amount >= 21 and transaction.amount < 500:
            return True
        return False

    def process(self, transaction):
        print(f'Process transaction with id {transaction.id}')
        print('Finished processing')


class CheapPaymentGateway(AbstractPaymentGateway):
    def is_available(self):
        randint = random.randint(1, 10)
        return randint > 5

    def can_process_transaction(self, transaction):
        if transaction.amount <= 20:
            return True
        return False

    def process(self, transaction):
        print(f'Process transaction with id {transaction.id}')
        print('Finished processing')


class PremiumPaymentGateway(AbstractPaymentGateway):
    def is_available(self):
        randint = random.randint(1, 10)
        return randint > 5

    def can_process_transaction(self, transaction):
        if transaction.amount > 500:
            return True
        return False

    def process(self, transaction):
        print(f'Process transaction with id {transaction.id}')
        print('Finished processing')
