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


class Context:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_strategy(self):
        return self.strategy


if __name__ == "__main__":
    print(issubclass(ConcreteStrategyA, StrategyInterface))
    print(issubclass(ConcreteStrategyB, StrategyInterface))
    print(issubclass(ConcreteStrategyC, StrategyInterface))
    print(ConcreteStrategyA.__mro__)

    context = Context()

    context.set_strategy(ConcreteStrategyA())
    print(context.get_strategy())

    context.set_strategy(ConcreteStrategyB())
    print(context.get_strategy())

    context.set_strategy(ConcreteStrategyC())
    print(context.get_strategy())
