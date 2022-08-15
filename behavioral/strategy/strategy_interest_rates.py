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
        print('\nInvesting in GIC (interest rate -', rate,' ): ', "${:,.2f}".format(sum_invest))
        print('Final Sum at end of year 1 (at maturity) : ', "${:,.2f}".format(sum_invest * (1 + rate)))


class InterestRatesHISA():
    def execute_strategy(self, sum_invest: float) -> None:
        rate = 0.01
        print('\nInvesting in HISA (interest rate -', rate,' ): ', "${:,.2f}".format(sum_invest))
        print('Final Sum at end of year 1 : ', "${:,.2f}".format(sum_invest * (1 + rate)))
        gains = (sum_invest * (1 + rate)) - sum_invest
        for i in range(0, 12):
            print('sum paid on month [', i + 1, '] : ', "${:,.2f}".format(gains / 12))


class InterestRatesTFSA():
    def execute_strategy(self, sum_invest: float) -> None:
        rate = 0.025
        print('\nInvesting in TFSA (interest rate -', rate,' ): ', "${:,.2f}".format(sum_invest))
        print('Invested for 3 years, capitalized annually')
        print('Final Sum at end of year 3 : ', "${:,.2f}".format(sum_invest * (1 + rate)**3))


class InvestmentAccount:
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
    invest = InvestmentAccount()

    invest.set_strategy(InterestRatesGIC())
    invest.execute(sum_to_invest)

    invest.set_strategy(InterestRatesHISA())
    invest.execute(sum_to_invest)

    invest.set_strategy(InterestRatesTFSA())
    invest.execute(sum_to_invest)
