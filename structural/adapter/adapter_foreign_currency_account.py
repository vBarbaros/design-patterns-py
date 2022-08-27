class AccountsEuroCurrencyInterface:
    def deposit_euro(self, init_deposit): pass


class AccountsEuroCurrency(AccountsEuroCurrencyInterface):
    def __init__(self, init_deposit):
        self.current_balance = init_deposit

    def deposit_euro(self, amount_to_deposit):
        print('Balance before: [EURO', self.current_balance, ']')
        print('... depositing: [EURO', amount_to_deposit, ']')
        self.current_balance += amount_to_deposit
        print('Balance after: [EURO', self.current_balance, ']')


class AccountsCanadianDollarCurrency:
    def deposit(self, amount_to_deposit): pass


# Class Adapter
class CanToEuroConverterClassType(AccountsCanadianDollarCurrency, AccountsEuroCurrency):
    def __init__(self, init_deposit):
        super().__init__(init_deposit)
        self.can_to_euro_exchange_rate = 0.7752

    def deposit(self, amount_to_deposit_in_can):
        amount_to_deposit_in_euro = self.can_to_euro_exchange_rate * amount_to_deposit_in_can
        self.deposit_euro(amount_to_deposit_in_euro)


# Object Adapter
class CanToEuroConverterObjectType(AccountsCanadianDollarCurrency):
    def __init__(self, adaptee):
        self.adaptee = adaptee
        self.can_to_euro_exchange_rate = 0.7752

    def deposit(self, amount_to_deposit_in_can):
        amount_to_deposit_in_euro = self.can_to_euro_exchange_rate * amount_to_deposit_in_can
        self.adaptee.deposit_euro(amount_to_deposit_in_euro)


class BankOfCanada:
    __adapter = None

    def __init__(self, adapter):
        self.__adapter = adapter

    def deposit(self, amount_to_deposit):
        self.__adapter.deposit(amount_to_deposit)


def main_class_adapter_pattern():
    print('\n...running Class Adapter Patter')
    client = BankOfCanada(CanToEuroConverterClassType(1000))
    client.deposit(500)


def main_object_adapter_pattern():
    print('\n...running Object Adapter Patter')
    adapter = CanToEuroConverterObjectType(AccountsEuroCurrency(1000))
    client = BankOfCanada(adapter)
    client.deposit(500)


if __name__ == "__main__":
    main_class_adapter_pattern()
    main_object_adapter_pattern()
