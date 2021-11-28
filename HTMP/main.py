import htmp

project1 = htmp.Web('/home/guertinu/Desktop', 'DocForHtmp')
page1 = project1.init('index')

html = htmp.Html(page1)

html.Header['title']('Document')
html.Header['charset']('utf-8')