# import StringCompare class and unittest library
import unittest
from QuestionB import StringCompare


class TestStrings(unittest.TestCase):

    # TESTS for Greater Function
    # The equal test
    def test1_ForGreater(self):
        strings = StringCompare('1.2', '1.1')
        self.assertEqual(strings.greater(), '1.2 is greater than 1.1')

    # The assertTrue test
    def test2_ForGreater(self):
        strings = StringCompare('1.1', '1.01')
        self.assertTrue(strings.greater(), '1.1 is greater than 1.01')

    # The NotEqual test
    def test3_ForGreater(self):
        strings = StringCompare('-2.1', '-3.45')
        self.assertNotEqual(strings.greater(), '-3.45 is greater than -2.1')



    # TESTS for Lesser Function
    # The equal test
    def test1_ForLesser(self):
        strings = StringCompare('1.1', '1.2')
        self.assertEqual(strings.lesser(), '1.1 is lesser than 1.2')

    # The assertTrue test
    def test2_ForLesser(self):
        strings = StringCompare('1.1', '1.01')
        self.assertTrue(strings.lesser(), '1.01 is lesser than 1.1')

    # The NotEqual test
    def test3_ForLesser(self):
        strings = StringCompare('-2.1', '-3.45')
        self.assertNotEqual(strings.lesser(), '-2.1 is lesser than -3.45')



    # TESTS for Equal Function
    # The equal test 1
    def test1_ForEqual(self):
        strings = StringCompare('1.1', '1.2')
        self.assertEqual(strings.equal(), '1.2 is not equal to 1.1')

    # The equal test 2
    def test2_ForEqual(self):
        strings = StringCompare('1.1', '1.1')
        self.assertEqual(strings.equal(), '1.1 is equal to 1.1')

    # The NotEqual test
    def test3_ForNotEqual(self):
        strings = StringCompare('1.1', '1.3')
        self.assertNotEqual(strings.equal(), '1.1 not equal 1.3')


# main method
if __name__ == '__main__':
    unittest.main()
