# source : https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_strategy.htm
# with small adaptations to keep same style across examples


class AbstractionA:
    def operation_imp(self, impl_property):
        print(f'Abstraction Instance A is producing using property = {impl_property}')


class AbstractionB:
    def operation_imp(self, impl_property):
        print(f'Abstraction Instance B is producing using property = {impl_property}')


class Implementation:
    def __init__(self, impl_property, abstraction):
        """Initialize the necessary attributes
        Implementation independent Abstraction"""
        self._property = impl_property
        self._abstraction = abstraction

    def produce(self):
        """Implementation specific Abstraction"""
        self._abstraction.operation_imp(self._property)

    def expand(self, times):
        """Implementation independent Abstraction"""
        self._property = self._property * times


if __name__ == "__main__":
    impl1 = Implementation('alpha', AbstractionA())
    impl1.produce()

    impl2 = Implementation('beta', AbstractionB())
    impl2.produce()
