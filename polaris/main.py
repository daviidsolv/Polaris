import flet as ft
from flet import icons
from drinks import Drinks

drinkTypes = [
    ft.NavigationDestination(icon=icons.EXPLORE, label="REFRESCOS"),
    ft.NavigationDestination(icon=icons.EXPLORE, label="BIRRA"),
    ft.NavigationDestination(icon=icons.EXPLORE, label="CUBATAS"),
    ft.NavigationDestination(icon=icons.EXPLORE, label="CUBATAS XL"),
    ft.NavigationDestination(icon=icons.EXPLORE, label="CHUPITOS"),
]

ticket = []

class Drink:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def getDataRow(self):
        return ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(self.name)),
                ft.DataCell(ft.Text(self.qty)),
                ft.DataCell(ft.Text(self.price))
            ]
        )

def main(page: ft.Page):
    def addDrinkToTicket(drink):
        ticket.append(drink)
        existingRows = page.get_table_data(ticketSection)

    def generateDrinkSelection(drinkType):
        return ft.Container(
            content=Drinks.getDrinksGrid(drinkType),
            #bgcolor=ft.colors.RED,
            width=9999,
            height=200,
        )
    
    drinkSelection = generateDrinkSelection("refrescos")

    def tabChanged(e):
        tabIndex = e.data
        drinkMap = ["refrescos", "birra", "cubatas", "cubatas xl", "chupitos"]

        drinkSelection.content = Drinks.getDrinksGrid(drinkMap[int(tabIndex)])
        page.update()
        print("tabChanged")

    def fabClick(e):
        print("fabClick " + e.data)

    page.floating_action_button = ft.FloatingActionButton(
        icon=icons.CAMERA,
        on_click=fabClick,
    )

    page.title = "NavigationBar Example"
    page.navigation_bar = ft.NavigationBar(
        label_behavior=ft.NavigationBarLabelBehavior.ALWAYS_HIDE,
        destinations=Drinks.getDrinksNavigationDestinations(),
        on_change=tabChanged
    )

    table = ft.Container(
        content=ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Articulo")),
                ft.DataColumn(ft.Text("Cantidad")),
                ft.DataColumn(ft.Text("Precio")),
            ],
            rows=[
                Drink("birra", 1, "1.50").getDataRow(),
                Drink("roncola", 3, "5.50").getDataRow(),
                Drink("ginlemon", 2, "5.50").getDataRow(),
                Drink("chupito 1€", 1, "1.00").getDataRow(),
                Drink("chupito MES", 4, "3.00").getDataRow(),
            ],
            column_spacing=10,
        ),
        width=999,
    )

    ticketSection = ft.ListView(
        expand=1,
        spacing=10,
        auto_scroll=False,
        controls=[
            table,
        ]
    )

    body = ft.Column(
        controls=[ticketSection, drinkSelection],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True,
    )

    page.add(ft.SafeArea(body, expand=True))

    page.update()

ft.app(target=main)