class ChangeHtmlTxt:

    def __init__(self, txt: str):
        self.txt = txt
        self.allChar = {
            'sup': '^^',
            'sub': '^',
            'strong': '**',
            'em': '\\',
            'mark': '#',
            'u': '__',
            'strike': '--',
        }

    def _replaceHtml(self, char, balise):
        b = self.txt.split(char)
        for i in b[1::2]:
            self.txt = self.txt.replace(f'{char}{i}{char}', f'<{balise}>{i}</{balise}>')
        return self.txt

    def change(self):
        for balise in self.allChar:
            char = self.allChar.get(balise)
            self.txt = self._replaceHtml(char, balise)
        return self.txt

    def htmlspacialchar(self, *char):
        for chars in char:
            self.txt = self.txt.replace(chars, '')
        return self.txt