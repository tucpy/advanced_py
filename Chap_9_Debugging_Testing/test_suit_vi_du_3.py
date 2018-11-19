def tinh_tong(a,b):
    return a + b

import unittest

class TestMedthods(unittest.TestCase):
    def runTest(self):
        self.assertEqual(tinh_tong(3,4),7)
        self.assertEqual(tinh_tong(2,3),5)
        self.assertEqual(tinh_tong(5,4),9)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TestMedthods())
        return suite

if __name__=="__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)