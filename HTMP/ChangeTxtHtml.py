import re

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

    def changeBalise_a(self, url: list):
        txt = self.txt.split(':')
        txt2 = txt[1::2]
        if len(txt2) == len(url):
            for i, word in enumerate(txt2):
                txt2[i] = f"<a href='{url[i]}'>"+str(word)+"</a>"
                self.txt = re.sub(rf':{word}:', f'{txt2[i]}', self.txt, count=1)
            return self.txt
        else:
            return 'error'
