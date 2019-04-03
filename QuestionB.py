# This class compares two strings with three methods: greater, lesser and equal
class StringCompare:
    # Constructor
    def __init__(self, firstString, secondString):
        self.num1 = float(firstString)
        self.num2 = float(secondString)

    # Greater than Function
    def greater(self):
        condition = self.num1 > self.num2
        return "{0} is greater than {1}".format(self.num1, self.num2) if condition else \
               "{0} is greater than {1}".format(self.num2, self.num1)

    # Less than Function
    def lesser(self):
        condition = self.num1 < self.num2
        return "{0} is lesser than {1}".format(self.num1, self.num2) if condition else \
               "{0} is lesser than {1}".format(self.num2, self.num1)
    # Equal to  Function
    def equal(self):
        condition = self.num1 == self.num2
        return "{0} is equal to {1}".format(self.num1, self.num2) if condition else \
               "{0} is not equal to {1}".format(self.num2, self.num1)
