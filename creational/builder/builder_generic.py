class Builder:
    def build_part(self): pass


class ConcreteBuilder(Builder):
    def build_part(self):
        print('build part A')
        print('build part B')
        print('build part C')
        return self.get_result()

    def get_result(self):
        return 'Final Built (part A, part B, Part C)'


class Director():
    def __init__(self, builder):
        self.builder = builder
        self.result = ''

    def construct(self):
        self.result = self.builder.build_part()

    def show_result(self):
        print(self.result)


def main_object_builder_pattern():
    print('...creating Director...')
    adapter = Director(ConcreteBuilder())
    print('...calling constructor()...')
    adapter.construct()
    print('...displaying the built result...')
    adapter.show_result()


if __name__ == "__main__":
    main_object_builder_pattern()
