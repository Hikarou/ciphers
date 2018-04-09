# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
from ciphers_helper import functions as f


class Vigenere:
    def __init__(self, key, verbose=False):
        self.key = key
        self.verbose = verbose

    def _decipher_char(self, char: chr, key_letter: chr) -> chr:
        """
        Helper for decipher one char
        :rtype: chr
        :param char: The char to decipher
        :param key_letter: The key to decipher with
        :return: The deciphered char
        """
        c = f.get_position(char)
        shift = f.get_position(key_letter)
        if c == -1:
            return ''
        m = chr(ord('A') + (c - shift) % (ord('Z') - ord('A') + 1))
        return m

    def decipher_string(self, string: str) -> str:
        """
        Decipher a string using the key given in constructor
        :rtype: str
        :param string: The string to decipher
        :return: The deciphered string
        """
        clear = ''
        key_length = len(self.key)
        for i, c in enumerate(string):
            clear += self._decipher_char(c, self.key[i % key_length])
        if self.verbose:
            print(clear)
        return clear

    def cipher_char(self, char: chr, key_letter: chr) -> chr:
        """
        Helper for cipher one char
        :param char: The char to cipher
        :rtype: chr
        :param key_letter: The key to cipher with
        :return: The ciphered char
        """
        m = f.get_position(char)
        shift = f.get_position(key_letter)
        if m == -1:
            return ''
        c = chr(ord('A') + (m + shift) % (ord('Z') - ord('A') + 1))
        return c

    def cipher_string(self, string: str) -> str:
        """
        Cipher a string using the key given in constructor
        :rtype: str
        :param string: The string to cipher
        :return: The ciphered string
        """
        ciphered = ''
        key_length = len(self.key)
        for i, c in enumerate(string):
            ciphered += self.cipher_char(c, self.key[i % key_length])
        if self.verbose:
            print(ciphered)
        return ciphered
