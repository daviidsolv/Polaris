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

    page.window_width = 1170 /4        # window's width is 200 px
    page.window_height = 2532 /4      # window's height is 200 px
    page.window_resizable = False  # window is not resizable

    page.title = "NavigationBar Example"
    page.navigation_bar = ft.NavigationBar(
        destinations=Drinks.getDrinksNavigationDestinations(),
    )

    ticketSection = ft.Container(
        content=ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Articulo")),
                ft.DataColumn(ft.Text("Cantidad")),
                ft.DataColumn(ft.Text("Precio")),
            ],
            column_spacing=10,
        ),
        width=page.window_width,
    )

    drinkSelection1 = ft.Container(
        content=ft.ElevatedButton("birra"),
        bgcolor=ft.colors.RED,
        width=page.window_width,
        height=200,
    )

    body = ft.Column(
        controls=[ticketSection, drinkSelection1],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True,
    )

    page.add(body)

    page.update()

ft.app(target=main)