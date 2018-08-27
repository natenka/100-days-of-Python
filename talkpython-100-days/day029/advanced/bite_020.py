class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        while self.balance < 0:
            self._transactions.pop()

### full rollback
    def __enter__(self):
        self._transactions_copy = list(self._transactions)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.balance < 0:
            print('Balance below 0, rolling back transaction')
            self._transactions = self._transactions_copy
