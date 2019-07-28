import unittest
import kitbarashi

class TestKitbarashi(unittest.TestCase):
    def test_barashi(self):
        o = kitbarashi.Kitbarashi()
        self.assertEqual([{"item":1, "qty":2, "price":100}], o.barashi(1,2,100) )