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
|^^|^|**|\|#|__|--|:
|^^text^^|^text^|**text\*\*|\\text\\|#text#|__text\_\_|--text--|:text:|
|<sup>text|<sub>text|<strong>text|<em>text|<mark>text|<u>text|<strike>text|<a>text|

---
####example :

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
####for link...

---
```python
# add parameter 'a_path=' for add html file.
page1_html.Body["p"]("on :click:", a_path=[page2_html])
```

* **Important:** the files will be in the <u>order you defined</u>
```python
page1_html.Body["p"](":one: :two: :three: [etc..]", a_path=[one_file, tow_file, three_file])
```

---
---
###About

* create by ```WinstonWolf007```
* version ```4```

---
* when to use this module ? ```For write speed html code```