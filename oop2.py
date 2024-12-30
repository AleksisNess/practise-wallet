class Wallet:

    def __init__(self, valuta='Unknown', name='Unknown'):
        if valuta not in ('USD', 'EUR'):
            raise ValueError ('The exact currency is not specified (Either USD or EUR)')
        
        self.__money_dollar = 0.0
        self.__money_euro = 0.0
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany, valuta):
        if valuta == 'USD':
            self.__money_dollar += howmany
        else:
            self.__money_euro += howmany
        
    def top_down_balance(self, howmany, valuta):
        
        if valuta == 'USD':
            if self.__money_dollar - howmany < 0:
                raise ValueError ('There are not enough funds in the account to make the transaction')
            self.__money_dollar -= howmany
        else:
            if self.__money_euro - howmany < 0:
                raise ValueError ('There are not enough funds in the account to make the transaction')
            self.__money_euro -= howmany


    def info(self, valuta):
        if valuta == 'USD':
            print(self.__money_dollar, '$')
        else:
            print(self.__money_euro, '€')    

x = Wallet('USD', 'Ivan')
x.top_up_balance(200, 'USD')
x.top_up_balance(500, 'EUR')
x.info('USD')
x.info('EUR')
print()
x.top_down_balance(30, 'USD')
x.top_down_balance(75, 'EUR')
x.info('USD')
x.info('EUR')
