class Caesar:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet2 ="эьормщднйгычясюцажшбтпвёле0узхкфи"
    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = dict()  # TODO
        for i in range(len(self.alphabet2)):
            letter = self.alphabet2[i]
            decoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._decode[letter] = decoded
            self._decode[letter.upper()] = decoded.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._decode.get(char, char) for char in line])


key = int(input('Введите ключ:'))
cipher = Caesar(key)
line = ''
line += input()
#while line[-4:] != 'stop':
    #line += input()
while line:
    print(cipher.decode(line))
    line = input()