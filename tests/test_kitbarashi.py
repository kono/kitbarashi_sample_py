import unittest
import kitbarashi

class TestKitbarashi(unittest.TestCase):
    def test_get_price_index(self):
        r =  {"kitcode":2, "price_ar":[120,110,100,0]}
        o = kitbarashi.Kitbarashi()
        self.assertEqual((0,1) , o.get_price_index(r, 120))

        r = [
            {"item": 91, "qty": 1, "price": 120},
            {"item": 92, "qty": 1, "price": 80}
        ]
        self.assertEqual(r, o.get_kit_component(9,1,0,1))

    def test_barashi(self):
        o = kitbarashi.Kitbarashi()
        self.assertEqual([{"item":1, "qty":2, "price":100}], o.barashi(1,2,100) )

        r = [
            {"item": 10, "qty": 1, "price":40},
            {"item": 11, "qty": 2, "price":20},
            {"item": 12, "qty": 1, "price":40}
        ]
        self.assertEqual(r, o.barashi(2, 1, 120))

        r2 = [
            {"item": 10, "qty": 2, "price":30},
            {"item": 11, "qty": 4, "price":20},
            {"item": 12, "qty": 2, "price":40}
        ]
        self.assertEqual(r2, o.barashi(2, 2, 110))
