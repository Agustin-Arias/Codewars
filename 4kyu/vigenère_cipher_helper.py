# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.len = len(alphabet)

    def encode(self, text):
        encoded_text = ""
        key_index = 0
        for letter in text:
            print(f"letter: {letter}")
            if not letter in self.alphabet:
                encoded_text += letter
            else:
                index_letter = self.alphabet.index(letter)
                key_index_add = self.alphabet.index(self.key[key_index])
                encoded_text += self.alphabet[(index_letter + key_index_add) % self.len]
            key_index += 1
            key_index = key_index % len(self.key)
        return encoded_text

    def decode(self, text):
        decoded_text = ""
        key_index = 0
        for letter in text:
            if not letter in self.alphabet:
                decoded_text += letter
            else:
                index_letter = self.alphabet.index(letter)
                key_index_add = self.alphabet.index(self.key[key_index])
                decoded_text += self.alphabet[(index_letter - key_index_add) % self.len]
            key_index += 1
            key_index = key_index % len(self.key)
        return decoded_text


abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

print(c.encode("encoding it's a shift cipher!"))
