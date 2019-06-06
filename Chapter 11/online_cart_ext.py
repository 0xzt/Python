class ItemToPurchase():
    def __init__(self, itemName='none', itemPrice=0, itemQuant=0):
        self.item_name = str(itemName)
        self.item_price = float(itemPrice)
        self.item_quantity = int(itemQuant)
        self.item_description = itemDesc
    
    def print_item_cost(self):
        self.total = int(self.item_price * self.item_quantity)
        return ('%s %d @ $%.0f = $%d' % (self.item_name, self.item_quantity, self.item_price, self.total))

class ShoppingCart():
    def __init__(self, cust_name='none', c_date='January 1, 2016'):
        self.customer_name = cust_name
        self.current_date = c_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
    
    def remove_item(self, itemName):
        not_found = True
        for n in self.cart_items:
            if n.item_name == itemName:
                self.cart_items.remove(n)
                not_found = False
        if not_found:
            print('Item not found in cart. Nothing removed.')
    
    def modify_item(self, ItemToPurchase):
        not_found = True
        for n in self.cart_items:
            if n.item_name == ItemToPurchase.item_name:
                if n.item_price != 0:
                    n.item_price = float(input('Enter the new price:\n'))
                    not_found = False
                if n.itemQuant != 0:
                    n.item_quantity = int(input('Enter the new quantity:\n'))
                    not_found = False
                if n.item_description != 'none':
                    n.item_description = input('Enter the new description:\n')
                    not_found = False
        if not_found:
            print('Item not found in cart. Nothing modified.')
    
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    
    def get_cost_of_cart(self):
        grand_total = int()
        for n in self.cart_items:
            grand_total += int(n.item_price)
        return grand_total
    
    def print_num_items(self):
        print('Number of Items: {}\n'.format(len(self.cart_items)))
    
    def print_total(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}\n'.format(self.customer_name, self.current_date))
            self.print_num_items()
            for n in self.cart_items:
                print('%s %d @ $%.0f = $%d' % (n.item_name, n.item_quantity, n.item_price, n.total))
            print('\nTotal: ${}'.format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print('{}\'s Shopping Cart - {}\n'.format(self.customer_name, self.current_date))
        print('\nItem Descriptions')
        for n in self.cart_items:
            print('{}: {}'.format(n.item_name, n.item_description))
    
    def output_shopping_cart(self):
        print('OUTPUT SHOPPING CART')
        self.print_total()
    
    def output_items_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        self.print_descriptions()
    
    def add_item_to_cart(self):
        print('ADD ITEM TO CART')
        add_name = input('Enter the item name:\n')
        add_desc = input('Enter the item description:\n')
        add_price = input('Enter the item price:\n')
        add_quant = input('Enter the item quantity:\n')
        self.add_item(ItemToPurchase(add_name, add_desc, add_price, add_quant))
    
    def remove_item_from_cart(self):
        print('REMOVE ITEM FROM CART')
        item_to_remove = input('Enter name of item to remove:\n')
        remove_item(item_to_remove)
    
    def change_item_qty(self):
        print('CHANGE ITEM QUANTITY')
    
    def print_menu(self):
        print('\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items\' descriptions\no - Output shopping cart\nq - Quit\n')
        active = True
        while active:
            my_choice = input('Choose an option:\n')
            if my_choice == 'q':
                active = False
            elif my_choice == 'a':
                self.add_item_to_cart()
            elif my_choice == 'r':
                self.remove_item_from_cart()
            elif my_choice == 'c':
                pass
            elif my_choice == 'i':
                self.output_items_descriptions()
            elif my_choice == 'o':
                self.output_shopping_cart()

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
    c_name = input('Enter customer\'s name:\n')
    c_date = input('Enter today\'s date:\n')
    
    print('\nCustomer name: {}\nToday\'s date: {}'.format(c_name, c_date))
    my_cart = ShoppingCart(c_name, c_date)
    my_cart.print_menu()