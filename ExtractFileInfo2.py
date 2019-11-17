class ItemsPrice(object):
    """__init__() functions as the class constructor"""
    def __init__(self, item=None, price=None):
        self.item = item
        self.price = price


def get_info():
    itemsPrice = []
    linenum = 0
    matchedItems = "»"
    matchedPrice = "â‚¬"
    finalItems = []
    prevItem = ''
    prevPrice = ''
    with open ('outputbase.txt', 'rt') as myfile:
        for line in myfile:
            if line.lower().find(matchedItems) != -1:
                lineWOSymbol = line.split(' ')
                lineWOSymbol.pop(0)
                seperator = ' '
                curitem = seperator.join(lineWOSymbol)

            if line.lower().find(matchedPrice) != -1:
                text = line.split(' ')
                curprice = text[(len(text))-2].replace(',' , '.')
                itemsPrice.append(ItemsPrice(curitem, curprice))


    for item in itemsPrice:
        if prevItem == item.item:
            item.price = item.price + prevPrice
        else:
            item.price = item.price

        finalItems.append(ItemsPrice(item.item, item.price))
        prevItem = item.item
        prevPrice = item.price
    item = []
    price = []
    for finalItem in finalItems:
        item.append(finalItem.item.rstrip('\n'))
        price.append(finalItem.price)
    return item, price


item, price = get_info()
print(item)
print(price)

