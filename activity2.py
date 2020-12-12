class Phone(object):
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

    def prices(rec, phnname, model, price):
        rec.append(Phone(phnname, model, price))
        return rec

# Main Code
Record = []
x = 'y'
while x == 'y':
    phnname = input('Enter the name of the Phone: ')
    height = input('Enter the model number: ')
    model = input('price: ')
    Record = prices(Record, phnname, model, height)
    x = input('Another Phone? y/n: ')
# Printing the list of Phone
n = 1
print("---The list of the phone that store have---")
for el in Record:
    print (n, '.', el)
    n = n + 1
