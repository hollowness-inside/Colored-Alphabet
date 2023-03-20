from typing import Dict, List, Tuple


class Alphabet:
    letters: Dict[str, Tuple[int, List[int]]]

    def __init__(self):
        self.letters = {}

    def _add_letter(self, symbol: str, colors: List[int]) -> None:
        colors_num = len(colors)
        self.letters[symbol] = (colors_num, colors)


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
