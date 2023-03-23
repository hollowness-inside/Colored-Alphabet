import sys
from typing import Dict, List, Tuple

from PIL import Image, ImageColor

Hex = str
Colors = List[Hex]

class Alphabet:
    letters: Dict[str, Colors]

    def __init__(self):
        self.letters = {}

    def _add_letter(self, symbol: str, colors: Colors) -> None:
        colors_num = len(colors)
        self.letters[symbol] = colors

    def encode_char(self, char: str) -> Colors:
        if char.isupper():
            let1 = self.letters['UPPER']
            let2 = self.letters[char.lower()]

            return let1 + let2

        if char == ' ':
            return self.letters.get('SPACE', None)

        return self.letters.get(char, None)

    def encode_text(self, text: str) -> List[Colors]:
        encoded = []

        for char in text:
            color = self.encode_char(char)

            if color is None:
                print(f'Unknown letter "{char}"')
                encoded.append(["#000000"])
            else:
                encoded.append(color)

        return encoded


def load_alphabet(path: str) -> Alphabet:

    def readline():
        line = file.readline()
        if line == '':
            return None

        return [x.strip() for x in line.split('\t\t')]

    alph = Alphabet()

    with open(path, 'r') as file:
        column_colors = readline()

        for i, char in enumerate(readline()):
            alph._add_letter(char, [column_colors[i]])

        while (l := readline()) != None:
            row_color, l[0] = l[0].split('\t')

            for i, char in enumerate(l):
                alph._add_letter(char, [row_color, column_colors[i]])

    return alph


def square_image(alphabet: Alphabet, text: str) -> Image.Image:
    colors = alphabet.encode_text(text)
    colors = [hex for litra in colors for hex in litra]
    colors = [ImageColor.getcolor(x, 'RGB') for x in colors]

    img_size = int(len(colors)**0.5) + 1
    img = Image.new('RGB', (img_size, img_size), '#000000')
    img.putdata(colors)
    return img


def line_image(alphabet: Alphabet, text: str) -> Image.Image:
    colors = alphabet.encode_text(text)
    colors = [hex for litra in colors for hex in litra]
    colors = [ImageColor.getcolor(x, 'RGB') for x in colors]

    img_length = len(colors)
    img = Image.new('RGB', (img_length, 1), "#000000")
    img.putdata(colors)
    return img


if __name__ == '__main__':
    args = {'a': 'alphabet.txt'}
    it = iter(sys.argv)

    for i in it:
        if i == '-l':
            args['l'] = True
            continue

        if i.startswith('-'):
            args[i[1:]] = next(it)

    if args.get('o', None) == None:
        print(
            'Usage: python3 main.py (-f FILE_NAME) (-t SOME_TEXT) [-l] -o OUTPUT.png'
            '\n\t-l\tDraw colors in one row')
        exit()

    a = load_alphabet(args['a'])
    style = square_image

    if args.get('l', False):
        style = line_image

    if path := args.get('f', None):
        with open(path) as file:
            text = ' '.join(file.read().split('\n'))
            out = style(a, text)

    elif text := args.get('t', None):
        out = style(a, text)

    # out = out.resize((out.width*10, out.height*10), Image.Resampling.NEAREST)
    out.save(args['o'])
