from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition = None):
        super().__init__(condition)
        self.category = "Decor"

    def __str__(self):
        return "Something to decorate your space."