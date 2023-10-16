import flet as ft
from flet import icons

drinkTypes = [
    ft.NavigationDestination(icon=icons.EXPLORE, label="REFRESCOS"),
    ft.NavigationDestination(icon=icons.EXPLORE, label="BIRRA"),
    ft.NavigationDestination(icon=icons.EXPLORE, label="CUBATAS"),
    ft.NavigationDestination(icon=icons.EXPLORE, label="CUBATAS XL"),
    ft.NavigationDestination(icon=icons.EXPLORE, label="CHUPITOS"),
]

class HomeScreen(ft.Page):
    def __init__(self):
        super().__init__()
        self.title = "Home"
        self.title = "NavigationBar Example"
        self.navigation_bar = ft.NavigationBar(
            destinations=drinkTypes,
        )
    
    def run(self):
        print("HomeScreen run")

ft.app(HomeScreen())