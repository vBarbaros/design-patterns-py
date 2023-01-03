class Handler:
    """
    Abstract handler class
    """

    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle_request(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')


class ConcreteHandler1(Handler):
    """
    Concrete handler 1
    """

    def _handle(self, request):
        if 0 < request <= 10:
            print(f'Request {request} handled in handler 1')
            return True


class ConcreteHandler2(Handler):
    """
    Concrete handler 2
    """

    def _handle(self, request):
        if 10 < request <= 20:
            print(f'Request {request} handled in handler 2')
            return True


class ConcreteHandler3(Handler):
    """
    Concrete handler 3
    """

    def _handle(self, request):
        if 20 < request <= 30:
            print(f'Request {request} handled in handler 3')
            return True


class Client():
    def __init__(self, handler):
        self.handler = handler

    def handle_request(self, request_nr):
        # Send requests to the chain
        h3.handle_request(request_nr)


if __name__ == "__main__":
    # Build the chain of responsibility
    h1 = ConcreteHandler1()
    h2 = ConcreteHandler2(h1)
    h3 = ConcreteHandler3(h2)

    client = Client(h3)
    client.handle_request(5)
    client.handle_request(15)
    client.handle_request(25)
