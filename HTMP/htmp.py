import os
import ChangeTxtHtml
from Error import Error


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
                    file.write(codes)

    def init(self, name):
        name = name.replace(".", '')
        with open(os.getcwd() + '/' + self._project_name + '/' + f'{name}.html', 'w') as file:
            file.close()

        return {
            'file-name': name + '.html',
            'file-path': self._project_path + '/' + name + '.html',
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
            'charset': self._Header_charset
        }
        self.Body = {
            'h': self._Body_title,
            'p': self._Body_paragraph,
            'img': self._Body_image
        }

    def _Header_title(self, content: str):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>')
        generate = f"<title>{content}</title>"
        self._headerCode[5] = generate

    def _Header_charset(self, content: str):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>', '/')
        generate = f'<meta charset="{content}">'
        self._headerCode[3] = generate

    def _Body_title(self, size: int, content: str, *, id_=None, class_=None, url_a: list = None):
        if 6 >= size >= 1:
            content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>', '/')
            content = ChangeTxtHtml.ChangeHtmlTxt(content).change()
            if url_a is not None:
                print('in')
                u = []
                for i in url_a:
                    u.append(i.source()[1])
                content = ChangeTxtHtml.ChangeHtmlTxt(content).changeBalise_a(url_a)
            generate = f"<h{size}>{content}</h{size}>"
            self._bodyCode.insert(self._idx_body, generate)
            self._idx_body += 1
        else:
            self._bodyCode.insert(self._idx_body, Error(0).returnError())
            self._idx_body += 1

    def _Body_paragraph(self, content: str, *, id_=None, class_=None, url_a: list = None):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('>', '<', '/')
        content = ChangeTxtHtml.ChangeHtmlTxt(content).change()
        if url_a is not None:
            u = []
            for i in url_a:
                u.append(i.source()[1])
            content = ChangeTxtHtml.ChangeHtmlTxt(content).changeBalise_a(u)
        generate = f"<p>{content}</p>"
        self._bodyCode.insert(self._idx_body, generate)
        self._idx_body += 1

    def _Body_image(self, url: str, *, id_=None, class_=None):
        url = ChangeTxtHtml.ChangeHtmlTxt(url).htmlspacialchar('>', '<')
        generate = f"<img src='{url}'>"
        self._bodyCode.insert(self._idx_body, generate)
        self._idx_body += 1

    def source(self):
        return [self._headerCode + self._bodyCode, self._file_name]