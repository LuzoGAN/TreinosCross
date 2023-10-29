import flet
from flet import *

class MainContainer(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        # Retorni basico title:subtitulo e UI
        return Container(
            width=275,
            height=60,
            content=Column(
                spacing=5,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(
                        'Treinos',
                        size=10,
                        weight='w400',
                        color='white',
                    ),
                    Text(
                        'Semana',
                        size=30,
                        weight='bold',
                        color='white'
                    )
                ]
            )
        )

class DropDownContainer(UserControl):
    def __init__(self, initials: str, name: str, gen: str, title: str, description: str, salary: str):
        super().__init__()
        self.initials = initials
        self.name = name
        self.gen = gen
        self.title = title
        self. description = description
        self.salary = salary

    def ExpandContainer(self, e):
        if self.controls[0].height != 180:
            self.controls[0].height = 180
            self.controls[0].update()
        else:
            self.controls[0].height = 90
            self.controls[0].update()

    def TopContainer(self):
        return Container(
            width=265,
            height=70,
            content=Column(
                spacing=0,
                controls=[
                    Row(
                        controls=[
                            Container(
                                width=40,
                                height=40,
                                bgcolor='white24', # cor do circulo das iniciais
                                border_radius=40,
                                alignment=alignment.center,
                                content=Text(
                                    self.initials,
                                    size=11,
                                    weight='bold',
                                ),
                            ),
                            VerticalDivider(width=2),
                            # Nome e subnome
                            Container(
                                content=Column(
                                    spacing=1,
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        Text(self.name, size=11, color='white'),
                                        Text(self.gen, size=9, color='white'),
                                    ]
                                )
                            )
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            Container(
                                content=IconButton(
                                    icon=icons.ARROW_DROP_DOWN_CIRCLE_ROUNDED,
                                    icon_size=20,
                                    on_click=lambda e: self.ExpandContainer(e),
                                )
                            )
                        ]
                    )
                ]
            ),
        )

    def GetEmployeeData(self):
        items = [
            ['Job Title', self.title],
            ['Description', self.description],
            ['Salary', self.salary],
        ]
        l = []

        for item in items:
            l.append(
                Row(
                    controls=[
                        Column(
                            expand=1, # 1:2 expand ratio
                            horizontal_alignment=CrossAxisAlignment.START,
                            controls=[
                                Text(
                                    item[0], # Primeiro elemento da lista
                                    size=9,
                                    width='bold',
                                    color='white'
                                )
                            ]
                        ),
                        Column(
                            expand=2,  # 1:2 expand ratio
                            horizontal_alignment=CrossAxisAlignment.END,
                            controls=[
                                Text(
                                    item[1],  # Primeiro elemento da lista
                                    size=9,
                                    width='bold',
                                    color='white54'
                                )
                            ]
                        )
                    ]
                )
            )
        return l

    def BottomContainer(self):
        title, description, salary = self.GetEmployeeData()
        return Container(
            width=265,
            height=100,
            content=Column(
                spacing=12,
                controls=[
                    # adicionar aqui
                    title,
                    description,
                    salary
                ]
            )
        )

    def build(self):
        return Container(
            width=275,
            height=90,
            bgcolor='white10',
            border_radius=11,
            animate=animation.Animation(400,'decelerate'),
            padding=padding.only(left=10, right=10, top=10),
            # clip behavior allown us to clip conents to the container
            # this cancels out the overflor but its contly production wise
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.TopContainer(),
                    self.BottomContainer()
                ]
            )
        )

def main(page: Page):
    page.title = 'Treinos Semana'
    page.vertical_aligment = MainAxisAlignment.CENTER
    page.horizontal_aligment = CrossAxisAlignment.CENTER

    main_container = Container(
        width=280,
        height=600,
        bgcolor='black',
        border_radius=40,
        padding=20,
        content=Column(
            scroll='hidden',
            # Adicionando as classes aqui
            controls=[
                # Divisores
                Divider(height=20, color='transparent'),
                MainContainer(),
                Divider(height=30, color='white'),
                Text('Employees', size=12),
                DropDownContainer('L.G',
                                  'Luzo Gomes',
                                  'Analista',
                                  'Junior',
                                  'I.C',
                                  '4000.00'),
                DropDownContainer('I.A',
                                  'Izadora de Jesus',
                                  'Analista',
                                  'Senior',
                                  'Cob',
                                  '5000.00'),
            ]

        )
    )
    page.add(main_container)
    page.update()
    pass

if __name__ == '__main__':
    flet.app(target=main)
