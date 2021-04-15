import string, random

class Round(object):
    def __init__(self, *seqs):
        self.position = 0
        self.data = [i for x in seqs for i in x]
        self.len = len(self.data)

    def __repr__(self):
        return str(self.data)

    def __iter__(self):
        self.position = 0
        return self

    def is_item(self, item):
        if str(self.data[self.position]) == str(item):
            return True
        return False

    def __getitem__(self, index):
        if index < self.len-1 and index >= 0:
            return self.data[index]
        else:
            while index < 0:
                index += self.len-1
            while index > self.len-1:
                index -= self.len-1
            return self.data[index]

    def next(self):
        if self.position >= self.len-1:
            self.position = 0
            raise StopIteration
        else:
            self.position += 1
            return self.data[self.position-1]

class JCripter(object):
    def __init__(self, string):
        self.string = string
        self.generate_key_set()
        self.encrypted = False

    def generate_key_set(self):
        self.alphabet = list(string.ascii_lowercase)
        self.numbers = [str(x) for x in range(10)]
        self.special_characters = ['"',"'",',','?','.',
                                   ' ','(',')',':',';',
                                   '!','@','#','$','%',
                                   '^','&','*','_','-',
                                   '+','=','<','>','~',
                                   '`','{','[','}',']',
                                   '\\','|']
        self.key_base = Round(self.alphabet, self.numbers, self.special_characters)

    def get_key_index(self, key):
        for i in self.key_base:
            if isinstance(key, int):
                if i == self.key_base[key]:
                    return self.key_base.position-1
            elif i == key.lower():
                return self.key_base.position-1
        else:
            print ("not found")

    def __repr__(self):
        return self.string

    def _encrypt(self, string, func, *args):
        if string == None:
            string = self.string
            if string == None:
                return
        string = string.lower()
        n_string = func(string, *args)
        self.encrypted = not self.encrypted
        self.string = n_string
        return n_string

class CeaserCypher(JCripter):
    def __init__(self, string, shift=None):
        JCripter.__init__(self, string)
        if shift == None:
            self.shift = random.randint(0, self.key_base.len)
        else:
            self.shift = shift

    def encrypt(self, string=None):
        def inner(string):
            n_string=''
            for i in string:
                if self.encrypted == True:
                    n_string += self.key_base[self.get_key_index(i)-self.shift]
                else:
                    n_string += self.key_base[self.get_key_index(i)+self.shift]
            return n_string
        return self._encrypt(string, inner)

class PseudoRandomCypher(JCripter):
    def __init__(self, string, shifts=None):
        if shifts == None:
            self.shift = [random.randint(0, 500) for x in string]
        else:
            self.shift = shifts
        JCripter.__init__(self, string)

    def encrypt(self, string=None):
        def inner(string):
            ind = 0
            n_string = ''
            for i in string:
                if ind >= len(self.shift)-1:
                    ind = 0
                if self.encrypted == True:
                    n_string += self.key_base[self.get_key_index(i)-self.shift[ind]]
                else:
                    n_string += self.key_base[self.get_key_index(i)+self.shift[ind]]
                ind += 1
            return n_string

        return self._encrypt(string, inner)

class PolyAlphabeticCypher(JCripter):
    def __init__(self, string, key, enc=False):
        JCripter.__init__(self, string)
        self.key=list(key)
        self.encrypted = enc

    def encrypt(self, string=None):
        def inner(string):
            index = 0
            n_string = ''
            for i in string:
                if index >= len(self.key)-1:
                    index = 0
                if self.encrypted == True:
                    n_string += self.key_base[self.get_key_index(i)-self.get_key_index(self.key[index])]
                else:
                    n_string += self.key_base[self.get_key_index(i)+self.get_key_index(self.key[index])]
                index += 1
            return n_string
        return self._encrypt(string, inner)