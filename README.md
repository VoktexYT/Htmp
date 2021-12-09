# H T M P

---
---
* **install and config**
* **init basic project with htmp**
* 
* **how edit html code**
* **how edit css code**
* **how edit Js code**
* 
* **html string shortcut**
* **all html markup**
* **all Js event**
* **all css event**
* 
* **code example**
* **about**
---
---

### [how install and config ?]
* For **install** module, click on green button "code" and download
* To **use** the module, choose the htmp manager and place it in your project
* To **try**, import it into your python file ```import htmp```

---
---

### [how use htmp ?]


* **import** htmp module
```python
from HTMP import htmp
```

---

* **init** your project
```python
project1 = htmp.Web("<path>", "<directory name>")
```
* ```<path>``` insert the path where the folder will be located with the html code
* ```<directory name>``` give the directory name
---

* **create** html file
```python
page1_html = htmp.Html(project1.init("<html name file>"))
```

* put the project variable and do ```'.init()``` to create the html file
* ```html name file``` give the html file name

---

* **load** your project
```python
all_file = [page1_html.source()]
project1.load(all_file)
```

* put all html page variable in the list ```.load([ this ])```
* don't forget ```.source() ``` '' at the end of the variable 
---
---

### [edit html page]
* create html file
```python
page1_html = htmp.Html(project1.init("index.html"))
```
* put the Charest
```python
page1_html.Header["charset"]("utf-8")
```

* put the title in the Header
```python
page1_html.Header["title"]("web site !")
```

* put the css link
```python
page1_html.Header["link"]([style1_css])
#                             ^ all variables which are css pages
```

* put the Js link
```python
# the script is situated IN THE HEADER
page1_html.Header["script"]([script1_js])

# the script is situated IN THE BODY
page1_html.Body["script"]([script1_js])
```

* put the title in the Body (h1, h2, h3, ...)
```python
page1_html.Body["h"](1, "this h1")
#                    ^ is size (1 to 6)
```

* put simple text
```python
page1_html.Body["p"]("this text")
```

* put image
```python
page1_html.Body["img"]("path or url")
```

* put **id** and **class**
```python
page1_html.Body["p"]('hello', id_='text')
page1_html.Body["p"]('bey', class_='txt')
page1_html.Body["p"]('this text', id_='text', class_='txt')
```

---
---

### [edit css page]
* create css page
```python
style_css = htmp.Css(project1.init("style.css"))
```

* edit css
```python
style_css.Style('id or class element', {
    'all css function': 'value',
    # example
    'color': 'red'
})
```

* add event
```python
style_css.Style('id or class element', {
    'color': 'red'
}, 'there event') # example: 'hover', 'focus', etc
```

* how get id or class ?
```python
textPage = page1_html.Body["p"]('hello', id_='text')

style_css.Style(textPage['id'], {
    [...]
})

# or (same thing with class) ('.name' or 'var['class']')

page1_html.Body["p"]('hello', id_='text')

style_css.Style('#text', {
    [...]
})

```

---
---

### [edit Js page]

* create js page
```python
script_js = htmp.Js(project1.init("script.js"))
```

* add event
```python
script_js.Event(
    '<event name>',
    '<who will trigger the event>',
    ['all the script that will be executed if the event is detected']
)
```

* add reflective code
```python
script_js.Event(
    '<event name>',
    '<who will trigger the event>',
    ['all the script that will be executed if the event is detected'],
    ['the reflective code']
)
```

* what is the reflective code ?
```
the reflective code is the code that will be run to Conversely the 'normal' code
```
---
---

### [string shotcut]
|Sup|Sub|Bold|italic|Highlight|under-line|center-line|link|
|---|---|----|------|---------|----------|-----------|----|
|^^ |^  |**  |\\    |#        |__        |\-\-       |:   |
|^^text^^|^text^|**text\*\*|\\text\\ |#text#|__text\_\_|--text--|:text:|
|<sup>text|<sub>text|<strong>text|<em>text|<mark>text|<u>text|<strike>text|<a>text|

---
#### example :

---
* I eat **an apple\*\*
* I eat **an apple**
---
* \#write# to the code in __your ide\_\_
* <mark>write</mark> to the code in <u>your ide</u>
---
* your \text\ ^is^ very ^^good^^ !
* your <em>text</em> <sub>is</sub> very <sup>good</sup> !
---
#### for link...

---
```python
# add parameter 'url_a=' for add html file.
page1_html.Body["p"]("on :click:", url_a=[page2_html])
```

* **Important:** the files will be in the <u>order you defined</u>
```python
page1_html.Body["p"](":one: :two: :three: [etc..]", url_a=[one_file, tow_file, three_file])
```

---
---
### [code example]

```python
# import module
from HTMP import htmp

# create project
wiki_project = htmp.Web('/home/user/Desktop', 'Wiki_Code')

# create 3 file
index_html = htmp.Html(wiki_project.init('index.html'))
style_css = htmp.Css(wiki_project.init('style.css'))
script_js = htmp.Js(wiki_project.init('script.js'))

# edit html file
btn = index_html.Body['h'](1, 'click me', id_='btn')
txt = index_html.Body['p']('this text')

# edit css file
style_css.Style(btn['id'], {
    'color': 'grey',
    'background-color': 'black',
    'transition': '0.3s'
})

# change style if hover
style_css.Style(btn['id'], {
    'color': 'red'
}, 'hover')

# edit Js file
script_js.Event(
    'click',
    btn['id'],
    # this normal if onclick a fist time: run code
    [
        script_js.changeHtml(txt['id'], 'this very good text'),
        script_js.changeCss(txt['id'], 'color', 'green')
    ],
    # this reflected if onclick a second time: run code
    [
        script_js.changeHtml(txt['id'], 'this very bad text'),
        script_js.changeCss(txt['id'], 'color', 'red')
    ]
)
```

---
---
### [About]

* create by ```WinstonWolf007```
* version ```4```

---
* when to use this module ? ```For write speed html code```
