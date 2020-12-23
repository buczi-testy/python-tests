import HtmlTestRunner
import unittest
import calc
from unittest.mock import patch

#@unittest.skip("not neccesary tests")
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')


class TestCalculateMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #return 7/0
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_adding_1(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_adding_2(self):
        self.assertEqual(calc.add(2, -1), 1)

    def test_adding_3(self):
        self.assertEqual(calc.add(-2, -3), -5)

    def test_adding_4(self):
        with patch('calc.add') as mocked_add:
            mocked_add.return_value = 6
            self.assertEqual(calc.add(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))