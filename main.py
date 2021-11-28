from htmp.module import *

web2 = Web(debug=False)
web = Web(debug=False)

# create page 1
page1 = web.init('/home/guertinu/Desktop', 'index')
page2 = web.init('/home/guertinu/Desktop', 'index2')

html = Html(page1)
html2 = Html(page2)

# HEADER section
html.Header['title']('Document')

# BODY section
html.Body['h'](6, 'salut')

# load code
web.run(page1)
web2.run(page2)