class Stock:
    def __init__(self, ticker, name):
        self.ticker = ticker
        self.name = name

    def get_ticker(self):
        return self.ticker

    def get_name(self):
        return self.name


s = Stock("005930", "삼성전자")
print(s.get_ticker())
print(s.get_name())
#print(s.ticker)
#print(s.name)
