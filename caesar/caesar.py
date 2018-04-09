# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
from ciphers_helper import functions as f


class Caesar:
    def __init__(self, key, verbose=False):
        self.key = key
        self.verbose = verbose

    def _decipher_char(self, char):
        c = f.get_position(char)
        if c == -1:
            return ''
        m = chr(ord('A') + (c - self.key) % (ord('Z') - ord('A') + 1))
        return m

    def decipher_string(self, string):
        clear = ''
        for c in string:
            clear += self._decipher_char(c)
        if self.verbose:
            print(clear)
        return clear

    def _cipher_char(self, char):
        m = f.get_position(char)
        if m == -1:
            return ''
        c = chr(ord('A') + (m + self.key) % (ord('Z') - ord('A') + 1))
        return c

    def cipher_string(self, string):
        ciphered = ''
        for c in string:
            ciphered += self._cipher_char(c)
        if self.verbose:
            print(ciphered)
        return ciphered

# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# KLMNOPQRSTUVWXYZABCDEFGHIJ