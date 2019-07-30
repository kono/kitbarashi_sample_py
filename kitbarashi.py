import kitmaster

class Kitbarashi:
    kitprice = (
        {"kitcode":2, "price_ar":[120,110,100,0]},
        {"kitcode":9, "price_ar":[200,230,250,210]}
     )

    def __init__(self):
        master = kitmaster.Kitmaster()
        self.kittable = master.kittable

    def iskit(self, item):
        return_val = False
        for r in self.kitprice:
            if ("kitcode", item) in r.items():
                return_val = True
        return return_val


    def barashi(self, item, qty, price):
        b = False
        a = self.iskit (item)
        if  a == False:
            b ={"item":item, "qty":qty, "price":price}
        return [b]
