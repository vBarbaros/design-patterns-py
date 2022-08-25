class AdapteeInterface:
    def specific_request(self, adapter_type): pass


class Adaptee(AdapteeInterface):
    def specific_request(self, adapter_type):
        print('A veru specific request -', adapter_type)


class Target:
    def request(self, adapter_type): pass


# Class Adapter
class AdapterClass(Target, Adaptee):
    def request(self, adapter_type):
        self.specific_request(adapter_type)


# Object Adapter
class AdapterObject(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self, adapter_type):
        self.adaptee.specific_request(adapter_type)


class Client:
    __adapter = None

    def __init__(self, adapter):
        self.__adapter = adapter

    def run(self, adapter_type):
        self.__adapter.request(adapter_type)


def main_class_adapter_pattern():
    adapter_type = 'Class Adapter Patter'
    client = Client(AdapterClass())
    client.run(adapter_type)


def main_object_adapter_pattern():
    adapter_type = 'Object Adapter Patter'
    adapter = AdapterObject(Adaptee())
    client = Client(adapter)
    client.run(adapter_type)


if __name__ == "__main__":
    main_class_adapter_pattern()
    main_object_adapter_pattern()
