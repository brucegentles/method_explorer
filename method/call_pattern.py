__author__ = 'abg'


class CallPattern:
    """
    class to contain the current touch list, and the means to manipulate it.
    """
    PLAIN_CODE = 0
    BOB_CODE = 1
    SINGLE_CODE = 2
    codes = []
    leads = ["plain", "bob", "single"]
    base = len(leads)
    size = 0
    single_offset = 0
    single_spacing = 14
    bob_spacing = 5

    def __init__(self, single_offset=0, single_spacing=14, length=60):
        """Initialise a TouchSet of length"""
        self.length = length
        self.codes = []
        self.more = True
        for i in range(length):
            self.codes.append(0)
        self.size = length * len(self.leads)
        self.single_offset = single_offset
        self.single_spacing = single_spacing

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
        n = len(self.codes)
        for i in range(n):
            self.codes[i] = self.PLAIN_CODE
        if False:
            for i in range(0, n, self.bob_spacing * 3):
                self.codes[i + self.bob_spacing * 0] = self.BOB_CODE
                self.codes[i + self.bob_spacing * 1] = self.BOB_CODE
                self.codes[i + self.bob_spacing * 2] = self.SINGLE_CODE
        if True:
            for i in range(0, n, self.bob_spacing):
                self.codes[i + 3] = self.BOB_CODE
                self.codes[i + 4] = self.SINGLE_CODE
                # self.codes[i+5] = self.SINGLE_CODE

        # for i in range(self.single_spacing,n,self.single_spacing):
        #    self.codes[i] = self.SINGLE_CODE

        calls = []
        for code in self.codes:
            calls.append(self.leads[code])
        return calls
