import os
import ChangeTxtHtml


class Web:

    def __init__(self, project_path, project_name):
        self._project_path = project_path
        self._project_name = project_name
        os.chdir(self._project_path)
        try:
            os.mkdir(self._project_name)
        except FileExistsError:
            pass

    def init(self, name):
        name = name.replace(".", '')
        with open(os.getcwd()+'/'+self._project_name+'/'+f'{name}.html', 'w') as file:
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
        self._file_name = page['file-name']
        self._file_path = page['file-path']
        self._directory_name = page['directory-name']
        self._directory_path = page['directory-path']

        self._charset = '<none>'
        self.idx_body = 1

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

        }

    def _Header_title(self, content: str):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>')
        generate = f"<title>{content}</title>"
        self._headerCode[5] = generate

    def _Header_charset(self, content: str):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>', '/')
        generate = f'<meta charset="{content}">'
        self._headerCode[3] = generate

    def _Body_title(self, size: int, content: str, *, id_=None, class_=None):
        content = ChangeTxtHtml.ChangeHtmlTxt(content).htmlspacialchar('<', '>', '/')
        if 6 >= size >= 1:
            content = ChangeTxtHtml.ChangeHtmlTxt(content).change()
            generate = f"<h{size}>{content}</h{size}>"
            self._bodyCode.insert(self.idx_body, generate)
            self.idx_body += 1
        else:
            self._bodyCode.insert(self.idx_body, Error(0).returnError())