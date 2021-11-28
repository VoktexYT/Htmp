import htmp

project1 = htmp.Web('/home/guertinu/Desktop', 'DocForHtmp')

index_html = htmp.Html(project1.init('index'))

index_html.Header['title']('salut')

for i in range(10):
    index_html.Body['h'](8, 'salut')


all_page = [index_html.source()]
project1.load(all_page)