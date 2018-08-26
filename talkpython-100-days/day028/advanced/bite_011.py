from functools import total_ordering


@total_ordering
class Account:
    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def _validate(self, amount):
        if not isinstance(amount, int):
            raise ValueError

    def __getitem__(self, position):
        return self._transactions[position]

    def __len__(self):
        return len(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, amount):
        self._validate(amount)
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._validate(amount)
        self._transactions.append(-amount)

    def __str__(self):
        return f'{self.name} account - balance: {self.balance}'


checking = Account('Checking')
saving = Account('Saving', 10)


#def test_account_balance():
assert checking.start_balance == 0
checking + 10
checking.balance == 10
print('checking.balance', checking.balance)

assert saving.start_balance == 10
saving - 5
assert saving.balance == 5


#def test_account_comparison():
assert checking > saving
assert checking >= saving
assert saving < checking
assert saving <= checking
saving + 5
assert checking == saving


#def test_account_len():
checking + 10
checking + 3
checking - 8
assert len(checking) == 4


#def test_account_indexing_iter():
assert checking[0] == 10
assert checking[-1] == -8
assert list(checking) == [10, 10, 3, -8]


#def test_account_str():
assert str(checking) == 'Checking account - balance: 15'
assert str(saving) == 'Saving account - balance: 10'
saving + 5
assert str(saving) == 'Saving account - balance: 15'

