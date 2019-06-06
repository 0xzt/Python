class ItemToPurchase():
    def __init__(self, itemName='none', itemPrice=0, itemQuant=0):
        self.item_name = str(itemName)
        self.item_price = float(itemPrice)
        self.item_quantity = int(itemQuant)
    
    def print_item_cost(self):
        self.total = int(self.item_price * self.item_quantity)
        return ('%s %d @ $%.0f = $%d' % (self.item_name, self.item_quantity, self.item_price, self.total))

def newItem():
    a = input('Enter the item name:\n')
    b = float(input('Enter the item price:\n'))
    c = int(input('Enter the item quantity:\n'))
    return ItemToPurchase(a, b, c)

def total_cost(itemList):
    my_total = 0
    print('\nTOTAL COST')
    for n in itemList:
        print(n.print_item_cost())
        my_total += n.total
    print('\nTotal: ${}'.format(my_total))

if __name__ == "__main__":
    item_count = 1
    item_list= []

    print('Item {}'.format(item_count))
    item_list.append(newItem())
    item_count += 1

    print('\nItem {}'.format(item_count))
    item_list.append(newItem())
    item_count += 1

    total_cost(item_list)

