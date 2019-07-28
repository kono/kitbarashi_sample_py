import kitmaster

class Kitbarashi:
    def __init__(self):
        master = kitmaster.Kitmaster()
        self.kitprice = master.kitprice
        self.kittable = master.kittable

    def barashi(self, item, qty, price):
        b ={"item":item, "qty":qty, "price":price}
        return [b]
