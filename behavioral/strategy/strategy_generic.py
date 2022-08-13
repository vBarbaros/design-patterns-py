import abc


class StrategyInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(self, subclass):
        return (hasattr(subclass, 'execute_strategy') and
                callable(subclass.execute_strategy))

    @abc.abstractmethod
    def execute_strategy(self, attribute: str) -> str:
        raise NotImplementedError


class ConcreteStrategyA():
    def execute_strategy(self, attribute: str) -> None:
        """Overrides StrategyInterface.algorithm_interface()"""
        print('strategy ', attribute)


class ConcreteStrategyB():
    def execute_strategy(self, attribute: str) -> None:
        """Overrides StrategyInterface.algorithm_interface()"""
        print('strategy ', attribute)


class ConcreteStrategyC():
    def execute_strategy(self, attribute: str) -> None:
        """Overrides StrategyInterface.algorithm_interface()"""
        print('strategy ', attribute)


class Context:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: StrategyInterface):
        self.strategy = strategy

    def execute(self, attribute: str):
        return self.strategy.execute_strategy(attribute)


if __name__ == "__main__":
    print(issubclass(ConcreteStrategyA, StrategyInterface))
    print(issubclass(ConcreteStrategyB, StrategyInterface))
    print(issubclass(ConcreteStrategyC, StrategyInterface))
    print(ConcreteStrategyA.__mro__)

    context = Context()

    context.set_strategy(ConcreteStrategyA())
    context.execute('A')

    context.set_strategy(ConcreteStrategyB())
    context.execute('B')

    context.set_strategy(ConcreteStrategyC())
    context.execute('C')
