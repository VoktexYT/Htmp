"""# import du module htmp
import htmp

project1 = htmp.Web('/home/guertinu/Desktop', 'DocForHtmp')
index_html = htmp.Html(project1.init('index'))

all_page = [index_html.source()]
project1.load(all_page)"""

# https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdtNZOP4Kmi8cbq8dxhRHfBWZI6ySIE5vXAw&usqp=CAU

import htmp

nintendoDescribe = htmp.Web('/home/guertinu/Desktop', 'nintendo')

mario_html = htmp.Html(nintendoDescribe.init('mario'))
luigi_html = htmp.Html(nintendoDescribe.init('luigi'))

################################
mario_html.Header['charset']('utf-8')
mario_html.Header['title']('bio mario')
mario_html.Body['h'](1, 'bio de mario')
mario_html.Body['p']('**clique** :ici: pour voir #la bio de __luigi__#', url_a=[luigi_html])
mario_html.Body['img']('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdtNZOP4Kmi8cbq8dxhRHfBWZI6ySIE5vXAw&usqp=CAU')

luigi_html.Header['charset']('utf-8')
luigi_html.Header['title']('bio luigi')
luigi_html.Body['h'](1, 'bio de luigi')
luigi_html.Body['p']('**clique** :ici: pour voir #la bio de __mario__#', url_a=[mario_html])
luigi_html.Body['img']('https://mario.wiki.gallery/images/thumb/7/72/MPSS_Luigi.png/170px-MPSS_Luigi.png')
################################
all_file = [mario_html.source(), luigi_html.source()]
nintendoDescribe.load(all_file)