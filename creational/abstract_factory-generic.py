from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactoryOne(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductAOne()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductBOne()


class ConcreteFactoryTwo(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductATwo()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductBTwo()


class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class ConcreteProductAOne(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product AOne."

class ConcreteProductATwo(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product ATwo."

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> None:
        pass


class ConcreteProductBOne(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product BOne."


class ConcreteProductBTwo(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product BTwo."


def client(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_a.useful_function_a()}")
    print(f"{product_b.useful_function_b()}")


if __name__ == "__main__":
    print("\nClient: Testing client code with Factory Type One:")
    client(ConcreteFactoryOne())

    print("\nClient: Testing client code with Factory Type Two:")
    client(ConcreteFactoryTwo())
