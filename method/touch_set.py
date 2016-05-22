__author__ = 'abg'


class TouchSet:
    """
    class to contain the current touch list, and the means to manipulate it.
    """

    codes = []
    leads = ["bob", "single"]
    base = len(leads)
    more = False
    size = 0

    def __init__(self, length=1):
        """Initialise a TouchSet of length"""
        self.length = length
        self.codes = []
        self.more = True
        for i in range(length):
            self.codes.append(0)
        self.size = length * len(self.leads)

    def inc(self):
        """
        increment the code by one.
        :return: None
        """
        carry = 1
        for idx in range(0, len(self.codes)):
            i = self.codes[idx] + carry
            carry = 0
            if i == self.base:
                carry = 1
                i = 0
            self.codes[idx] = i
            if carry == 0:
                break
        if carry == 1:
            self.more = False

    def print_codes(self):
        """ print the code for debug
        :return:
        """
        for i in range(len(self.codes)):
            print "codes[", i, "]=", self.codes[i]

    def get_code_txt(self):
        res = ""
        for i in self.codes:
            res += str.format("{:d}", i)

    def get(self):
        calls = []
        for i in self.codes:
            for j in range(4):
                calls.append("plain")
            calls.append(self.leads[i])
        return calls
