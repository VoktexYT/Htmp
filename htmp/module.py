from htmp.changeTxt import ChangeHtmlTxt
from htmp.error import Error

__all__ = ['Web', 'Html']


class Web:
    def __init__(self, debug=False):
        self._path = ''
        self.debug = debug
        self.code = ['<!DOCTYPE html>', '<html>', '<head>', '<meta charset="utf-8">', '<meta name="viewport" content="width=device-width, initial-scale=1">']

    def init(self, path, name):
        self._path = path+'/'+str(name)+'.html'
        return {
            "file-path": self._path,
            "file-name": str(name),
            "class-obj": self
        }

    def run(self, web_obj):
        self.code.append('</body>')
        self.code.append('</html>')
        with open(web_obj['file-path'], 'w') as file:
            for i in web_obj['class-obj'].code:
                file.write(i + "\n")

        print('\033[92mThe html site page is up to date!' if self.debug else '')


class Html:
    def __init__(self, web_obj):
        self._web_obj = web_obj
        self._file_path = self._web_obj['file-path']
        self._file_name = self._web_obj['file-name']
        self._class_obj = self._web_obj['class-obj']
        self.titleCreate = False

        self.Header = {
            'title': self._Header_title,
        }

        self.Body = {
            'h': self._Body_title,
            'p': self._Body_paragraph,
            'img': self._Body_image
        }

    def _Header_title(self, content: str):
        if not self.titleCreate:
            content = ChangeHtmlTxt(content).htmlspacialchar('<', '>')
            generate = f"<title>{content}</title>"
            self._web_obj['class-obj'].code.append(generate)
            self._web_obj['class-obj'].code.append('</head>')
            self._web_obj['class-obj'].code.append('<body>')
            self.titleCreate = True

    def checkTitle(self):
        if not self.titleCreate:
            self._Header_title(str(self._web_obj))

    def _Body_title(self, size: int, content: str, *, id_=None, class_=None):
        self.checkTitle()
        content = ChangeHtmlTxt(content).htmlspacialchar('<', '>', '/')

        if 6 >= size >= 1:
            content = ChangeHtmlTxt(content).change()
            generate = f"<h{size}>{content}</h{size}>"
            self._web_obj['class-obj'].code.append(generate)
        else:
            if self._web_obj['class-obj'].debug:
                self._web_obj['class-obj'].code.append(Error(0).returnError())

    def _Body_paragraph(self, content: str, *, id_=None, class_=None):
        self.checkTitle()
        content = ChangeHtmlTxt(content).htmlspacialchar('>', '<', '/')
        content = ChangeHtmlTxt(content).change()
        generate = f"<p>{content}</p>"
        self._web_obj['class-obj'].code.append(generate)

    def _Body_image(self, url: str, *, id_=None, class_=None):
        self.checkTitle()
        url = ChangeHtmlTxt(url).htmlspacialchar('>', '<')
        generate = f"<img src='{url}'>"
        self._web_obj['class-obj'].code.append(generate)