from flet import NavigationDestination, DataCell, DataRow, Text, icons, Image, ImageFit

drinks = [
    "REFRESCOS",
    "BIRRA",
    "CUBATAS",
    "CUBATAS XL",
    "CHUPITOS",
]

drinkIcons = [
    Image(
        src=f"/icons/icons8-reajuste-salarial-50.png",
        width=100,
        height=100,
        fit=ImageFit.CONTAIN,
    ),
    icons.EXPLORE,
    icons.EXPLORE,
    icons.EXPLORE,
    icons.EXPLORE,
]

class Drinks:
    def getDrinksList():
        return drinks
    
    def getDrinksNavigationDestinations():
        return [NavigationDestination(label=drink, icon_content=Text("test")) for drink in drinks]
    
class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getDrinkName(self):
        return self.name
    
    def getDrinkPrice(self):
        return self.price