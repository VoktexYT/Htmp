# H T M P

---
---
* **how install and config**
* **how use htmp**
* **how edit html code** 
* **string shortcut**
* **project example**
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

---

* **import** htmp module
```python
import htmp
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
page1_htnl = htmp.Html(project1.init("<html name file>"))
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

### [how edit html page ?]
* put the Charest
```python
page1_html.Header["charset"]("utf-8")
```

* put the title in the Header
```python
page1_html.Header["title"]("web site !")
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
### [Project Example]
```python
# import module
import htmp

# create project
wiki_project = htmp.Web('/home/guertinu/Desktop', 'Wiki_Code')

# create 3 html file (home.html), (python.html), (about.html)
home_html = htmp.Html(wiki_project.init('Home'))
python_html = htmp.Html(wiki_project.init('python'))
about_html = htmp.Html(wiki_project.init('about'))

# edit home file
home_html.Header['charset']('utf-8')
home_html.Header['title']('Home')
home_html.Body['h'](1, 'Home Page')
home_html.Body['p']('on **click** for __:about page:__ or __:python page:__', url_a=[about_html, python_html])

# edit python file
python_html.Header['charset']('utf-8')
python_html.Header['title']('Python')
python_html.Body['h'](1, 'Python page')
python_html.Body['p']('__python__ is **very good** programing #language#')
python_html.Body['p']('He is use in __the #artificial intelligence#__, __#web# site__, __video #game#__, etc')
python_html.Body['p']('on **click** for __:home page:__', url_a=[home_html])

# edit about file
about_html.Header['charset']('utf-8')
about_html.Header['title']('About')
about_html.Body['h'](1, 'About page')
about_html.Body['p']('this project \is created by\ WinstonWolf^^007^^')
about_html.Body['p']('on **click** for __:home page:__', url_a=[home_html])

# load all file
all_file = [home_html.source(), python_html.source(), about_html.source()]
wiki_project.load(all_file)
```

---
---
### [About]

* create by ```WinstonWolf007```
* version ```4```

---
* when to use this module ? ```For write speed html code```
