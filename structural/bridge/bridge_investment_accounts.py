# source : https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_strategy.htm
# with small adaptations to keep same style across examples


class client_account_debit:
    def operation_imp(self, impl_property):
        print(f'Abstraction Instance A is producing using property = {impl_property}')


class client_account_saving:
    def operation_imp(self, impl_property):
        print(f'Abstraction Instance B is producing using property = {impl_property}')

class client_account_credit:
    def operation_imp(self, impl_property):
        print(f'Abstraction Instance B is producing using property = {impl_property}')


class client_account_implementation:
    def __init__(self, impl_property, abstraction):
        """Initialize the necessary attributes
        Implementation independent Abstraction"""
        self._property = impl_property
        self._abstraction = abstraction

    def show_account_summary(self):
        """Implementation specific Abstraction"""
        self._abstraction.operation_imp(self._property)

    def expand(self, times):
        """Implementation independent Abstraction"""
        self._property = self._property * times


if __name__ == "__main__":
    impl1 = client_account_implementation('alpha', client_account_debit())
    impl1.show_account_summary()

    impl2 = client_account_implementation('beta', client_account_credit())
    impl2.show_account_summary()
