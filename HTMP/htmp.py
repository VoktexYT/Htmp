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
            f'\t<meta charset="{self._charset}">',
            '\t<meta name="viewport" content="width=device-width, initial-scale=1">',
            f'\t<title>{self._page}</title>',
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
            'link': self._Header_link,
            'script': self._Header_script
        }
        self.Body = {
            'h': self._Body_title,
            'p': self._Body_paragraph,
            'img': self._Body_image,
            'div': self._Body_div,
            'script': self._Body_script
        }

    def _Header_title(self, content: str):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>')
        generate = f"\t<title>{content}</title>"
        self._headerCode[5] = generate

    def _Header_charset(self, content: str):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>', '/')
        generate = f'\t<meta charset="{content}">'
        self._headerCode[3] = generate

    def _Header_link(self, content: list):
        for i in content:
            self._headerCode.insert(6, f'\t<link rel="stylesheet" type="text/css" href="{i.source()[1]}">')

    def _Header_script(self, content: list):
        for i in content:
            self._headerCode.insert(6, f'<script type="text/javascript" src="{i.source()[1]}"></script>')

    def _Body_script(self, content: list):
        for i in content:
            self._bodyCode.insert(1, f'\t<script type="text/javascript" src="{i.source()[1]}"></script>')

    def _Body_title(self, size: int, content: str, id_='', class_='', url_a: list = None):
        if 6 >= size >= 1:
            content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>', '/')
            content = ChangeTxtHtml.ChangeHtmlTxt(content).change()
            if url_a is not None:
                u = []
                for i in url_a:
                    u.append(i.source()[1])
                content = ChangeTxtHtml.ChangeHtmlTxt(content).changeBalise_a(url_a)
            generate = f"\t<h{size} id='{id_}' class='{class_}'>{content}</h{size}>"
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
        generate = f"\t<p id='{id_}' class='{class_}'>{content}</p>"
        self._bodyCode.insert(self._idx_body, generate)
        self._idx_body += 1
        return self._returnHtml(id_, class_, generate)

    def _Body_image(self, url: str, id_='', class_=''):
        url = ChangeTxtHtml.ChangeHtmlTxt(url).htmlspacialchar('>', '<')
        generate = f"\t<img src='{url}' id='{id_}' class='{class_}'>"
        self._bodyCode.insert(self._idx_body, generate)
        self._idx_body += 1
        return self._returnHtml(id_, class_, generate)

    def _Body_div(self, content: list, id_='', class_=''):
        all_html = []
        for i in content:
            all_html.append(i['struct'])
        generate = f"\t<div id='{id_}' class='{class_}'>{''.join(all_html)}</div>"
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

    def Style(self, obj, value: dict, event=False):
        if event and not obj+":"+str(event) in self._allCible:
            self._allCible[obj+":"+str(event)] = {}
        elif not event and not obj in self._allCible:
            self._allCible[obj] = {}
        if event:
            print(f'detected event !\n{str(event)=}\n{str(obj)=}\n{str(obj)+":"+str(event)}')
            newName = str(obj)+":"+str(event)
        for key_value in value:
            values = value[key_value]
            if event: self._allCible[newName][key_value] = values
            else: self._allCible[obj][key_value] = values

    def source(self):
        code = []
        code2 = []
        for key, value in self._allCible.items():
            for key2, value2 in self._allCible[key].items():
                code2.append(key2+': '+value2)
            comment = f'/*Change style of {key}*/'
            if ':' in key:
                comment = f"/*Change style of '{key.split(':')[0]}' if event '{key.split(':')[1]}:' is True*/"
            code.append(comment + "\n" + key + ' {\n\t' + ";\n\t".join(code2) + "\n}\n")

        return [code, self._file_name]


class Js:

    def __init__(self, page):
        self._page = page
        self._file_path = page['file-path']
        self._directory_name = page['directory-name']
        self._directory_path = page['directory-path']
        self._file_name = page['file-name']
        self._allCodeForInsert = []
        self._allCodeExisting = None

    def Event(self, event, obj, code: list, switch: list = False):
        if not switch:
            print(type(code))
            code.insert(0, "\t// this is '" + event + "' event")
            code = ';\n\t'.join(code)
            code += ';'
            if obj == 'window':
                self._allCodeForInsert.append('window.addEventListener("'+event+'", () => {\n'+code+'\n});')
            else:
                self._allCodeForInsert.append('document.querySelector("'+obj+'").addEventListener("'+event+'", () => {\n'+code+'\n});')
        else:
            code.insert(0, f"\t// this is '{event}' event")
            switch.insert(0, f"\t// this is reflected '{event}' event")
            code = ';\n\t\t'.join(code)
            code += ';'
            switch = ';\n\t\t'.join(switch)
            switch += ';'
            varName = event+'_'+obj[1:]
            generate = 'let '+varName+' = true;\n\n// he listen event '+event+'\ndocument.querySelector("'+obj+'").addEventListener("'+event+'", () => {\n\tif ('+varName+')\n\t{\n\t\t'+varName+' = false;\n\n\t'+code+'\n\t}\n\telse\n\t{\n\t\t'+varName+' = true;\n\n\t'+switch+'\n\t}\n});'
            self._allCodeForInsert.append(generate)

    def alert(self, content: str):
        return f'alert("{content}")'

    def consoleLog(self, content: str):
        return f'console.log("{content}")'

    def changeHtml(self, target, content: str):
        return f'document.querySelector("{target}").innerHTML = "{content}"'

    def changeCss(self, target, property_, newValue):
        return f'document.querySelector("{target}").style.{property_} = "{newValue}"'

    def source(self):
        return [self._allCodeForInsert, self._file_name]