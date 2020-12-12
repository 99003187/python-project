def __init__(self, phnname, model, price):
        self.phnname = phnname
        self.model = model
        self.price = price


def getprice(self):
    return self.price


def getmodel(self):
    return self.model


def __str__(self):
    return self.phnname + ' : ' +
    str(self.getmodel()) + ': :' + str(self.getprice())


def prices(phnname, model, price):
    return Record
Record = []
x = 'y'
while x == 'y':
    phnname = input('Enter the name of the Phone: ')
    height = input('Enter the model number: ')
    model = input('price: ')
    Record = (Record, phnname, model, height)
    x = input('Another Phone? y/n: ')
n = 1
for el in Record:
    print(n, ' . ', el)
    n = n + 2
