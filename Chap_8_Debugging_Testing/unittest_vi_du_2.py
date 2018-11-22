def tinh_tong(a,b):
    return a + b

import unittest

class TestMedthods(unittest.TestCase):
    def test1(self):
        self.assertEqual(tinh_tong(3,4),7)
    def test2(self):
        self.assertEqual(tinh_tong(2,3),5)
    def test3(self):
        self.assertEqual(tinh_tong(3,4),8)

if __name__=="__main__":
    unittest.main()