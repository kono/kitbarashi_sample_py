from kitmaster import kitmaster

class Kitbarashi:

    def __init__(self):
        master = kitmaster.Kitmaster()
        self.kittable = master.kittable()
        self.kitprice = master.kitprice()

    def iskit(self, item):
        return_val = None
        for r in self.kitprice:
            if ("kitcode", item) in r.items():
                return_val = r
        return return_val
    
    def get_price_index(self, kitprice_r, price):
        # ratio: If the price is not in the array, 
        # use the first element of the array to calculate the ratio
        # (code of calculating ratio has not implemented yet)
        ratio = 1
        return kitprice_r['price_ar'].index(price), ratio
    
    def get_kit_component(self, itemcode, p_qty, price_index, ratio):
        result = []
        for kit in self.kittable:
            if kit['kitcode'] == itemcode:
                price = kit['price_ar'][price_index] * ratio
                qty   = kit['qty'] * p_qty
                b = {"item": kit['linecode'], "qty": qty, "price": price}
                result.append(b)
        return result


    def barashi(self, item, qty, price):
        result =[]
        a = self.iskit (item)
        if  a is None:
            b ={"item":item, "qty":qty, "price":price}
            result.append(b)
        else:
                price_index, ratio = self.get_price_index(a, price)
                result = self.get_kit_component(item, qty, price_index, ratio)
        return result
