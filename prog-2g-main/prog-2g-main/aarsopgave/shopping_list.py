class ShoppingList:
    """
    En klasse til at repræsentere en indkøbsliste.

    Attributter
    -----------
    items : dict
        En ordbog til at gemme indkøbsvarer og deres mængder.

    Metoder
    -------
    add_item(item, quantity=1):
        Tilføjer en vare og dens mængde til indkøbslisten.
    
    remove_item(item, quantity=1):
        Fjerner en mængde af en vare fra indkøbslisten, hvis den findes.
    
    get_items():
        Returnerer ordbogen med indkøbsvarer og deres mængder.
    """
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
            else:
                del self.items[item]

    def get_items(self):
        return self.items

# Interaktivt eksempel på brug:
if __name__ == "__main__":
    shopping_list = ShoppingList()
    
    while True:
        action = input("Vil du tilføje (a), fjerne (r) en vare eller se listen (s)? (q for at afslutte): ").lower()
        
        if action == 'q':
            break
        elif action == 'a':
            item = input("Indtast varenavn: ")
            quantity = int(input("Indtast mængde: "))
            shopping_list.add_item(item, quantity)
        elif action == 'r':
            item = input("Indtast varenavn: ")
            quantity = int(input("Indtast mængde: "))
            shopping_list.remove_item(item, quantity)
        elif action == 's':
            print("Indkøbsliste:", shopping_list.get_items())
        else:
            print("Ugyldigt valg, prøv igen.")
