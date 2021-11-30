import htmp

nintendoDescribe = htmp.Web('/home/guertinu/Desktop', 'nintendo')

home_html = htmp.Html(nintendoDescribe.init('a'))
log_html = htmp.Html(nintendoDescribe.init('b'))
sign_html = htmp.Html(nintendoDescribe.init('c'))

#########################################################

home_html.Body['p'](':Log: == :Sign:', url_a=[log_html, sign_html])

log_html.Body['h'](1, 'connection a un compte')

sign_html.Body['h'](1, 'creation d un compte')

###########################################################

all_file = [home_html.source(), log_html.source(), sign_html.source()]
nintendoDescribe.load(all_file)