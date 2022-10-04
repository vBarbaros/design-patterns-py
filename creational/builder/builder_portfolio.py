class PortfolioBuilder:
    def build_part(self): pass
    def get_portfolio(self): pass


class IndexPortfolioBuilder(PortfolioBuilder):
    def build_index_portfolio(self):
        print('...add 40% shares from Canadian Index Fund')
        print('...add 30% shares from USA Index Fund')
        print('...add 30% shares from International Index Fund')
        return self.get_portfolio()

    def get_portfolio(self):
        return 'Your Portfolio (40% CAN, 30% US, 30% INT)'


class FinancialAdvisor():
    def __init__(self, portfolio_builder):
        self.portfolio_builder = portfolio_builder
        self.result = ''

    def construct(self):
        self.result = self.portfolio_builder.build_index_portfolio()

    def show_result(self):
        print(self.result)


def main_builder_pattern():
    print('...creating Director...')
    advisor = FinancialAdvisor(IndexPortfolioBuilder())
    print('...calling constructor()...')
    advisor.construct()
    print('...displaying the built result...')
    advisor.show_result()


if __name__ == "__main__":
    main_builder_pattern()
