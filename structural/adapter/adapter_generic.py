class AdapteeInterface:
    def specific_request(self): pass


class Adaptee(AdapteeInterface):
    def specific_request(self):
        print('I am requesting you to be very specific, here...')


class TargetInterface:
    def request(self): pass


class Target:
    def request(self): pass


# The Adapter
class Adapter(Adaptee, Target):
    def request(self):
        self.specific_request()


class Client:
    __adapter = None

    def __init__(self, adapter):
        self.__adapter = adapter

    def run(self):
        self.__adapter.request()


def main():
    adapter = Adapter()
    client = Client(adapter)
    client.run()


if __name__ == "__main__":
    main()
