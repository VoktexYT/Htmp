import ChangeTxtHtml

a = 'clicker :ici: pour se connecter ou bien :ici:'

b = ['index.html', 'index2.html']

a = ChangeTxtHtml.ChangeHtmlTxt(a).changeBalise_a(b)

print(a)