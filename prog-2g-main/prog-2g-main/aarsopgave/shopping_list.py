class ShoppingList:
   
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_items(self):
        return self.items

# Eksempel på brug:
if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add_item("Apples")
    shopping_list.add_item("Bananas")
    print(shopping_list.get_items())  # Output: ['Apples', 'Bananas']
    shopping_list.remove_item("Apples")
    print(shopping_list.get_items())  # Output: ['Bananas']
