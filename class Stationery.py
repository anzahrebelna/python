class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Start drawing.'

class Pen(Stationery):
    def draw(self):
        print(f'Starting pen drawing.')

class Pencil(Stationery):
    def draw(self):
        print(f'Start pencil drawing.')

class Handle(Stationery):
    def draw(self):
        print(f'Start handle drawing.')

pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')
pen.draw()
pencil.draw()
handle.draw()

