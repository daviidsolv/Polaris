from flet import NavigationDestination, DataCell, FilledButton, Text, GridView, Image, ImageFit

navBarIconSize = 45

class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getDrinkName(self):
        return self.name
    
    def getDrinkPrice(self):
        return self.price
    
    def getFilledButton(self):
        return FilledButton(text=self.name, on_click=(lambda e: print("Clicked " + self.name)))

drinks = [
    "REFRESCOS",
    "BIRRA",
    "CUBATAS",
    "CUBATAS XL",
    "CHUPITOS",
]

drinkIcons = [
    Image(src=f"/icons/icons8-reajuste-salarial-50.png", width=navBarIconSize, height=navBarIconSize, fit=ImageFit.CONTAIN),
    Image(src=f"/icons/icons8-cerveza-24.png", width=navBarIconSize, height=navBarIconSize, fit=ImageFit.CONTAIN),
    Image(src=f"/icons/icons8-cóctel-24.png", width=navBarIconSize, height=navBarIconSize, fit=ImageFit.CONTAIN),
    Image(src=f"/icons/icons8-cup-with-straw-50.png", width=navBarIconSize, height=navBarIconSize, fit=ImageFit.CONTAIN),
    Image(src=f"/icons/icons8-chupito-de-vodka-24.png", width=navBarIconSize, height=navBarIconSize, fit=ImageFit.CONTAIN),
]

drinkSelection = {
    "refrescos": [
        Drink("Coca Cola", 2.0),
        Drink("Agua", 2.0),
    ],
    "birra": [
        Drink("Barril", 2.0),
    ],
    "cubatas": [
        Drink("Cubata 4.5", 4.5),
        Drink("Cubata 5.5", 5.5),
        Drink("EXTRA REDBULL", 1.0),
    ],
    "cubatas xl": [
        Drink("Cubata XL 6.0", 6.0),
        Drink("Cubata XL 7.0", 7.0),
        Drink("EXTRA REDBULL", 1.0),
    ],
    "chupitos": [
        Drink("Chupito 1.0", 1.0),
        Drink("Chupito 2.0", 2.0),
        Drink("Chupito MES", 3.0),
    ],
}

class Drinks:
    def getDrinksList():
        return drinks
    
    def getDrinksNavigationDestinations():
        return [
            NavigationDestination(icon_content=drinkIcons[0]),
            NavigationDestination(icon_content=drinkIcons[1]),
            NavigationDestination(icon_content=drinkIcons[2]),
            NavigationDestination(icon_content=drinkIcons[3]),
            NavigationDestination(icon_content=drinkIcons[4]),
        ]
    
    def getDrinksGrid(drinkType):
        gv = GridView(
            expand=1,
            runs_count=5,
            max_extent=125,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5
        )

        gv.controls.clear()

        for i in range(0, len(drinkSelection[drinkType])):
            gv.controls.append(
                drinkSelection[drinkType][i].getFilledButton()
            )

        return gv
