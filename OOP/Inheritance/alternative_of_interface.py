class Book:

    def __init__(self,Writer) -> None:
        self.writer=Writer
    def category(self,name):
        raise NotImplementedError

class Nobel(Book):

    def __init__(self,writer) -> None:
        super().__init__(writer)
    def category(self, name):
        return f"Writer :{self.writer}\n Book Name : {name}"

Deyal=Nobel('Humayon Ahmed')
print(Deyal.category('Political Historycal Nobel'))

