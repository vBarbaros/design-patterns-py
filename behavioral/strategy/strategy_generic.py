# sources :
# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_strategy.htm
# https://realpython.com/python-interface/ (example of interface implementation in Python)

import abc


class StrategyInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(self, subclass):
        return (hasattr(subclass, 'algorithm_interface') and
                callable(subclass.algorithm_interface))

    @abc.abstractmethod
    def algorithm_strategy(self, attribute: str) -> str:
        raise NotImplementedError


class ConcreteStrategyA():
    def algorithm_interface(self, attribute: str) -> str:
        """Overrides StrategyInterface.algorithm_interface()"""
        pass


class ConcreteStrategyB():
    def algorithm_interface(self, attribute: str) -> str:
        """Overrides StrategyInterface.algorithm_interface()"""
        pass


class ConcreteStrategyC():
    def algorithm_interface(self, attribute: str) -> str:
        """Overrides StrategyInterface.algorithm_interface()"""
        pass


if __name__ == "__main__":
    print(issubclass(ConcreteStrategyA, StrategyInterface))
    print(issubclass(ConcreteStrategyB, StrategyInterface))
    print(issubclass(ConcreteStrategyC, StrategyInterface))
    print(ConcreteStrategyA.__mro__)
