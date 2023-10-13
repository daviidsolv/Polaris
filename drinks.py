from flet import NavigationDestination, DataCell, DataRow, Text, icons

drinks = [
    "REFRESCOS",
    "BIRRA",
    "CUBATAS",
    "CUBATAS XL",
    "CHUPITOS",
]

class Drinks:
    def getDrinksList():
        return drinks
    
    def getDrinksNavigationDestinations():
        return [NavigationDestination(label=drink, icon=icons.LOCAL_DRINK) for drink in drinks]
    
class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getDrinkName(self):
        return self.name
    
    def getDrinkPrice(self):
        return self.price