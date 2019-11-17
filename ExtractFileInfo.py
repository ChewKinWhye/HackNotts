class ItemsPrice(object):
    """__init__() functions as the class constructor"""
    def __init__(self, item=None, price=None):
        self.item = item
        self.price = price
        
def get_info(fileName):
    itemsPrice = []
    matchedItems = "»"
    matchedPrice = "â‚¬"
    finalItems = []
    with open (fileName, 'rt') as myfile:
        for line in myfile:
            if line.lower().find(matchedItems) != -1:
                lineWOSymbol = line.split(' ')
                lineWOSymbol.pop(0)
                seperator = ' '
                curitem = seperator.join(lineWOSymbol).rstrip('\n')

            if line.lower().find(matchedPrice) != -1:
                text = line.split(' ')
                curprice = text[(len(text))-2].replace(',' , '.')
                itemsPrice.append(ItemsPrice(curitem, curprice))


    for i in range(0, len(itemsPrice)):
        itemsPrice[i].price = float(itemsPrice[i].price)
        if(itemsPrice[i].item == itemsPrice[i-1].item):
            itemsPrice[i].price = itemsPrice[i].price + itemsPrice[i-1].price
    for i in range(0, len(itemsPrice)):
        if i < len(itemsPrice) -1:
            if(itemsPrice[i].item == itemsPrice[i+1].item):
                    del itemsPrice[i]
        if i < len(itemsPrice):
            finalItems.append(itemsPrice[i].item)
            finalItems.append(itemsPrice[i].price)
    return finalItems


# items1 = get_info('outputbase.txt')
# for i in items1:
#     print(i)
items2 = get_info('outputbase2.txt')
for i in items2:
    print(i)