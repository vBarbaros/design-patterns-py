from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractAccountFactory(ABC):
    @abstractmethod
    def create_savings_account(self) -> AbstractSavingsAccount:
        pass

    @abstractmethod
    def create_credit_account(self) -> AbstractCreditAccount:
        pass


class PlatinumAccountFactory(AbstractAccountFactory):
    def create_savings_account(self) -> AbstractSavingsAccount:
        return SavingsAccountPlatinum()

    def create_credit_account(self) -> AbstractCreditAccount:
        return CreditAccountPlatinum()


class GoldAccountFactory(AbstractAccountFactory):
    def create_savings_account(self) -> AbstractSavingsAccount:
        return SavingAccountGold()

    def create_credit_account(self) -> AbstractCreditAccount:
        return CreditAccountGold()


class AbstractSavingsAccount(ABC):
    @abstractmethod
    def confirm_savings_creation(self) -> str:
        pass


class SavingAccountGold(AbstractSavingsAccount):
    def confirm_savings_creation(self) -> str:
        return "Saving Gold Created."


class SavingsAccountPlatinum(AbstractSavingsAccount):
    def confirm_savings_creation(self) -> str:
        return "Saving Platinum Created."


class AbstractCreditAccount(ABC):
    @abstractmethod
    def confirm_credit_creation(self) -> str:
        pass


class CreditAccountGold(AbstractCreditAccount):
    def confirm_credit_creation(self) -> str:
        return "Credit Gold Created."


class CreditAccountPlatinum(AbstractCreditAccount):
    def confirm_credit_creation(self) -> str:
        return "Credit Platinum Created."


def client(factory: AbstractAccountFactory) -> None:
    savings_acc = factory.create_savings_account()
    credit_acc = factory.create_credit_account()

    print(f"{savings_acc.confirm_savings_creation()}")
    print(f"{credit_acc.confirm_credit_creation()}")


if __name__ == "__main__":
    print("\nClient: Testing client code with Platinum Account Factory:")
    client(PlatinumAccountFactory())

    print("\nClient: Testing client code with Gold Account Factory:")
    client(GoldAccountFactory())