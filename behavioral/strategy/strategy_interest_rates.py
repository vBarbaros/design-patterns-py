import abc


class InterestRatesInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(self, subclass):
        return (hasattr(subclass, 'execute_strategy') and
                callable(subclass.execute_strategy))

    @abc.abstractmethod
    def execute_strategy(self, sum_invest: float) -> None:
        raise NotImplementedError


class InterestRatesGIC():
    def execute_strategy(self, sum_invest: float) -> None:
        rate = 0.035
        print('Investing in GIC : ', "${:,.2f}".format(sum_invest))
        print('Final Sum at end of year 1 : ', "${:,.2f}".format(sum_invest*(1+rate)))
        gains = (sum_invest*(1+rate)) - sum_invest
        for i in range(0,12):
            print('sum paid on month [', i+1, '] : ', "${:,.2f}".format(gains / 12))


class InterestRatesHISA():
    def execute_strategy(self, sum_invest: float) -> None:
        rate = 0.01
        print('Investing in HISA: ', "${:,.2f}".format(sum_invest))
        print('Final Sum at end of year 1 : ', "${:,.2f}".format(sum_invest * (1 + rate)))
        gains = (sum_invest * (1 + rate)) - sum_invest
        for i in range(0, 12):
            print('sum paid on month [', i + 1, '] : ', "${:,.2f}".format(gains / 12))


class InterestRatesTFSA():
    def execute_strategy(self, sum_invest: float) -> None:
        rate = 0.025
        print('Investing in TFSA : ', "${:,.2f}".format(sum_invest))
        print('Final Sum at end of year 1 : ', "${:,.2f}".format(sum_invest * (1 + rate)))
        gains = (sum_invest * (1 + rate)) - sum_invest
        for i in range(0, 12):
            print('sum paid on month [', i + 1, '] : ', "${:,.2f}".format(gains / 12))


class BankAccount:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: InterestRatesInterface):
        self.strategy = strategy

    def execute(self, attribute: str):
        return self.strategy.execute_strategy(attribute)


if __name__ == "__main__":
    print(issubclass(InterestRatesGIC, InterestRatesInterface))
    print(issubclass(InterestRatesHISA, InterestRatesInterface))
    print(issubclass(InterestRatesTFSA, InterestRatesInterface))
    print(InterestRatesGIC.__mro__)

    sum_to_invest = 5000.0
    context = BankAccount()

    context.set_strategy(InterestRatesGIC())
    context.execute(sum_to_invest)

    context.set_strategy(InterestRatesHISA())
    context.execute(sum_to_invest)

    context.set_strategy(InterestRatesTFSA())
    context.execute(sum_to_invest)
