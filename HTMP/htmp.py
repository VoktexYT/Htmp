import os
import HTMP.ChangeTxtHtml as ChangeTxtHtml
from HTMP.Error import Error
import time
import string

time_ = 0.3
defaultJs = []

class Web:

    def __init__(self, project_path, project_name):
        self._project_path = project_path
        self._project_name = project_name
        os.chdir(self._project_path)
        try:
            os.mkdir(self._project_name)
        except FileExistsError:
            pass

        print(f"project creation: \033[92mOK\033[0m")
        time.sleep(time_)

    def load(self, code: list):
            for pageCode in code:
                try:
                    with open(self._project_path + '/' + self._project_name + '/' + pageCode[1], 'a') as file:
                        for codes in pageCode[0]:
                            file.write(str(codes)+'\n')
                    print(f"loading file '{pageCode[1]}': \033[92mOK\033[0m")
                    time.sleep(time_)
                except Exception as e:
                    print(f"loading file '{pageCode[1]}': \033[92m"+str(type(e)).split("'")[1]+"\033[0m")

    def init(self, name):
        try:
            name = name.split(".")
            check = string.ascii_letters + '0123456789' + '_'
            for i1 in name[0]:
                if i1 not in check:
                    raise SyntaxError
            for i2 in name[1]:
                if i2 not in check:
                    raise SyntaxError

            with open(os.getcwd() + '/' + self._project_name + '/' + f'{name[0]}.{name[1]}', 'w') as file:
                file.close()
            print(f"creating '{'.'.join(name)}' file: \033[92mOK\033[0m")
            time.sleep(time_)
        except Exception as e:
            print(f"creating '{'.'.join(name)}' file: \033[91m" + str(type(e)).split("'")[1] + "\033[0m")

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
            'script': self._Body_script,
            'input': self._Body_input,
            'form': self._Body_form
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

    def _Body_title(self, size: int, content: str, id_='', class_='', GET=False, url_a: list = None):
        if 6 >= size >= 1:
            content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>', '/')
            content = ChangeTxtHtml.ChangeHtmlTxt(content).change()
            if url_a is not None:
                u = []
                for i in url_a:
                    u.append(i.source()[1])
                content = ChangeTxtHtml.ChangeHtmlTxt(content).changeBalise_a(url_a)
            generate = f"\t<h{size} id='{id_}' class='{class_}'>{content}</h{size}>"
            return self._returnHtml(id_, class_, generate, GET)

        else:
            if not GET:
                self._bodyCode.insert(self._idx_body, Error(0).returnError())
                self._idx_body += 1
            return {'id': str(id_), 'class': str(class_)}

    def _Body_paragraph(self, content: str, id_='', class_='', GET=False, url_a: list = None):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('>', '<', '/')
        content = ChangeTxtHtml.ChangeHtmlTxt(content).change()
        if url_a is not None:
            u = []
            for i in url_a:
                if 'http' in i:
                    u.append(i)
                else:
                    u.append(i.source()[1])
            content = ChangeTxtHtml.ChangeHtmlTxt(content).changeBalise_a(u)

        generate = f"\t<p id='{id_}' class='{class_}'>{content}</p>"
        return self._returnHtml(id_, class_, generate, GET)

    def _Body_image(self, url: str, id_='', class_='', GET=False):
        url = ChangeTxtHtml.ChangeHtmlTxt(url).htmlspacialchar('>', '<')
        generate = f"\t<img src='{url}' id='{id_}' class='{class_}'>"
        return self._returnHtml(id_, class_, generate, GET)

    def _Body_div(self, content: list, id_='', class_='', GET=False):
        all_html = []
        for i in content:
            all_html.append(i['struct'])
        generate = f"\t<div id='{id_}' class='{class_}'>{''.join(all_html)}</div>"
        return self._returnHtml(id_, class_, generate, GET)

    def _Body_input(self, type_, property_: dict = False, id_='', class_='', GET=False):
        all_prop = []
        if property_:
            for key in property_:
                all_prop.append(f'{str(key)}="{str(property_[key])}"')
        generate = f'<input type="{type_}" id="{id_}" class="{class_}" {" ".join(all_prop)}>'
        return self._returnHtml(id_, class_, generate, GET)

    def _Body_form(self, action, method, input_: list, GET=False, id_='', class_=''):
        all_input = []
        for i in input_:
            all_input.append(i['struct'])
        generate = f'<form action="{action}" method="{method}">\n\t'+"\n\t".join(all_input)+'\n</form>'
        return self._returnHtml(id_, class_, generate, GET)

    def source(self):
        for i in defaultJs:
            self._bodyCode.insert(self._idx_body, i)
            self._idx_body += 1
        return [self._headerCode + self._bodyCode, self._file_name]

    def _returnHtml(self, id_, class_, generate, GET: bool):
        if not GET:
            self._bodyCode.insert(self._idx_body, generate)
            self._idx_body += 1
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
            newName = str(obj)+":"+str(event)
        for key_value in value:
            values = value[key_value]
            if event: self._allCible[newName][key_value] = values
            else: self._allCible[obj][key_value] = values

    def source(self):
        code = []
        #code2 = []
        for key, value in self._allCible.items():
            if ':' in key:
                code.append(f"/*change style of '{key.split(':')[0]}' if event '{key.split(':')[1]}:' is True*/")
            else:
                code.append(f'/*change style of {key}*/')
            code.append(key+' {')
            for key2, value2 in self._allCible[key].items():
                code.append('\t' + str(key2)+': '+ str(value2)+';')
            code.append('}\n')
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
        self._idx_prompt = 0

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

    def changeHtml(self, target, content: str):
        return f'document.querySelector("{target}").innerHTML = "{content}"'

    def changeCss(self, target, newValue: dict):
        allStyle = []
        for key in newValue:
            value = newValue[key]
            allStyle.append(f'document.querySelector("{target}").style.{key} = "{value}"')
        return "\n".join(allStyle)

    def changeProperty(self, target, property):
        prop = {
            '#': f'document.querySelector("{target}").id = "{property[1:]}"',
            '.': f'document.querySelector("{target}").className = "{property[1:]}"'
        }

        return prop.get(property[0]) if not None else 'Error'

    def source(self):
        return [self._allCodeForInsert, self._file_name]

    def debug(self, command):
        getKey = {
            'consoleLog': self._consoleLog,
            'alert': self._alert,
            'prompt': self._prompt,
            'htmlLog': self._htmlLog
        }

        return getKey.get(command)

    def _alert(self, content: str):
        generate = f'alert("{content}");'
        self._allCodeForInsert.append(generate)
        return generate

    def _consoleLog(self, content: str):
        generate = f'console.log("{content}");'
        self._allCodeForInsert.append(generate)
        return generate

    def _htmlLog(self, content: str):
        generate = f'<p>{content}</p>'
        defaultJs.append(generate)