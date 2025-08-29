from rich.console import Console
from rich.style import Style
from rich.table import Table

console = Console()
style = Style(color='blue', bgcolor='yellow')
console.print('привет', style=style)

countries = ['Россия', 'Италия']

table = Table(title='Страны')
table.add_column('Номер')
table.add_column('Название', style='yellow')

for number, country in enumerate(countries, start=1):
    table.add_row(str(number), country)
console.print(table)


class RichView():

    def print(self, text):
        console = Console()
        style = Style(color='blue', bgcolor='yellow')
        console.print(text, style=style)

    def print_tasks(self, tasks: list):
        table = Table(title='Список дел')
        table.add_column('Номер')
        table.add_column('Название', style='yellow')

        for number, name in enumerate(tasks, start=1):
            table.add_row(str(number), name)
        console.print(table)


view = RichView()
view.print('какой-то текст')
view.print_tasks(['первая задача', 'еще задача'])