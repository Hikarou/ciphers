# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
from ciphers_helper import functions as f


class Vigenere:
    def __init__(self, key, verbose=False):
        self.key = key
        self.verbose = verbose

    def _decipher_char(self, char, key_letter):
        c = f.get_position(char)
        shift = f.get_position(key_letter)
        if c == -1:
            return ''
        m = chr(ord('A') + (c - shift) % (ord('Z') - ord('A') + 1))
        return m

    def decipher_string(self, string):
        clear = ''
        key_length = len(self.key)
        for i, c in enumerate(string):
            clear += self._decipher_char(c, self.key[i % key_length])
        if self.verbose:
            print(clear)
        return clear

    def cipher_char(self, char, key_letter):
        m = f.get_position(char)
        shift = f.get_position(key_letter)
        if m == -1:
            return ''
        c = chr(ord('A') + (m + shift) % (ord('Z') - ord('A') + 1))
        return c

    def cipher_string(self, string):
        ciphered = ''
        key_length = len(self.key)
        for i, c in enumerate(string):
            ciphered += self.cipher_char(c, self.key[i % key_length])
        if self.verbose:
            print(ciphered)
        return ciphered
