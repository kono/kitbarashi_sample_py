from kitmaster import kitmaster

class Kitbarashi:

    def __init__(self):
        master = kitmaster.Kitmaster()
        self.kittable = master.kittable()
        self.kitprice = master.kitprice()

    def iskit(self, item):
        return_val = False
        for r in self.kitprice:
            if ("kitcode", item) in r.items():
                return_val = True
        return return_val


    def barashi(self, item, qty, price):
        result =[]
        a = self.iskit (item)
        if  a == False:
            b ={"item":item, "qty":qty, "price":price}
            result.append(b)
        return result
