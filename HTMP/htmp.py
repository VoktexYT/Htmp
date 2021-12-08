import os
import HTMP.ChangeTxtHtml as ChangeTxtHtml
from HTMP.Error import Error


class Web:

    def __init__(self, project_path, project_name):
        self._project_path = project_path
        self._project_name = project_name
        os.chdir(self._project_path)
        try:
            os.mkdir(self._project_name)
        except FileExistsError:
            pass

    def load(self, code: list):
        for pageCode in code:
            with open(self._project_path + '/' + self._project_name + '/' + pageCode[1], 'a') as file:
                for codes in pageCode[0]:
                    file.write(str(codes)+'\n')

    def init(self, name):
        name = name.split(".")
        with open(os.getcwd() + '/' + self._project_name + '/' + f'{name[0]}.{name[1]}', 'w') as file:
            file.close()

        return {
            'file-name': name[0] + '.' + name[1],
            'file-path': self._project_path + '/' + name[0] + '.' + name[1],
            'directory-path': self._project_path,
            'directory-name': self._project_name
        }


class Html:
    def __init__(self, page):
        self._page = page
        self._file_path = page['file-path']
        self._directory_name = page['directory-name']
        self._directory_path = page['directory-path']
        self._file_name = page['file-name']

        self._charset = '<none>'
        self._idx_body = 1

        self._headerCode = [
            '<!DOCTYPE html>',
            '<html>',
            '<head>',
            f'<meta charset="{self._charset}">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            f'<title>{self._page}</title>',
            '</head>'
        ]
        self._bodyCode = [
            '<body>',
            '</body>',
            '</html>'
        ]

        self.Header = {
            'title': self._Header_title,
            'charset': self._Header_charset,
            'link': self._Header_link
        }
        self.Body = {
            'h': self._Body_title,
            'p': self._Body_paragraph,
            'img': self._Body_image,
            'div': self._Body_div
        }

    def _Header_title(self, content: str):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>')
        generate = f"<title>{content}</title>"
        self._headerCode[5] = generate

    def _Header_charset(self, content: str):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>', '/')
        generate = f'<meta charset="{content}">'
        self._headerCode[3] = generate

    def _Header_link(self, content: list):
        for i in content:
            self._headerCode.insert(6, f'<link rel="stylesheet" type="text/css" href="{i.source()[1]}">')

    def _Body_title(self, size: int, content: str, id_='', class_='', url_a: list = None):
        if 6 >= size >= 1:
            content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>', '/')
            content = ChangeTxtHtml.ChangeHtmlTxt(content).change()
            if url_a is not None:
                print('in')
                u = []
                for i in url_a:
                    u.append(i.source()[1])
                content = ChangeTxtHtml.ChangeHtmlTxt(content).changeBalise_a(url_a)
            generate = f"<h{size} id='{id_}' class='{class_}'>{content}</h{size}>"
            self._bodyCode.insert(self._idx_body, generate)
            self._idx_body += 1
            return self._returnHtml(id_, class_, generate)

        else:
            self._bodyCode.insert(self._idx_body, Error(0).returnError())
            self._idx_body += 1
            return {'id': str(id_), 'class': str(class_)}

    def _Body_paragraph(self, content: str, id_='', class_='', url_a: list = None):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('>', '<', '/')
        content = ChangeTxtHtml.ChangeHtmlTxt(content).change()
        if url_a is not None:
            u = []
            for i in url_a:
                u.append(i.source()[1])
            content = ChangeTxtHtml.ChangeHtmlTxt(content).changeBalise_a(u)
        generate = f"<p id='{id_}' class='{class_}'>{content}</p>"
        self._bodyCode.insert(self._idx_body, generate)
        self._idx_body += 1
        return self._returnHtml(id_, class_, generate)

    def _Body_image(self, url: str, id_='', class_=''):
        url = ChangeTxtHtml.ChangeHtmlTxt(url).htmlspacialchar('>', '<')
        generate = f"<img src='{url}' id='{id_}' class='{class_}'>"
        self._bodyCode.insert(self._idx_body, generate)
        self._idx_body += 1
        return self._returnHtml(id_, class_, generate)

    def _Body_div(self, content: list, id_='', class_=''):
        print(content)
        all_html = []
        for i in content:
            all_html.append(i['struct'])
        generate = f"<div id='{id_}' class='{class_}'>{''.join(all_html)}</div>"
        self._bodyCode.insert(self._idx_body, generate)
        self._idx_body += 1
        return self._returnHtml(id_, class_, generate)

    def source(self):
        return [self._headerCode + self._bodyCode, self._file_name]

    def _returnHtml(self, id_, class_, generate):
        dict_choise = {
            "['', '']": {'id': '', 'class': '', 'struct': generate},
            f"['{id_}', '']": {'id': '#' + str(id_), 'class': '', 'struct': generate},
            f"['', '{class_}']": {'id': '', 'class': '.' + str(class_), 'struct': generate}
        }
        choise = dict_choise.get(str([id_, class_]))
        return choise if choise is not None else {'id': f'#{id_}', 'class': f'.{class_}', 'struct': generate}


class Css:

    def __init__(self, page):
        self._page = page
        self._file_path = page['file-path']
        self._directory_name = page['directory-name']
        self._directory_path = page['directory-path']
        self._file_name = page['file-name']
        self._allCible = {}

    def _checkCible(self, obj):
        return obj in self._allCible

    def Style(self, obj, value: dict):
        if not obj in self._allCible:
            self._allCible[obj] = {}
        for key_value in value:
            values = value[key_value]
            self._allCible[obj][key_value] = values

    def source(self):
        code = []
        code2 = []
        for key, value in self._allCible.items():
            for key2, value2 in self._allCible[key].items():
                code2.append(key2+': '+value2)
            code.append(key + '{' + ";".join(code2) + "}")

        return [code, self._file_name]
