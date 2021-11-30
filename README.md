# H T M P

---
---
* **how install and config**
* **how use htmp**
* **how edit html code** 
* **string shortcut**
* **project example**
* **credit**
---
---

### how install and config
* For **install** module, click on green button "code" and download
* To **use** the module, choose the htmp manager and place it in your project
* To **try**, import it into your python file

---

### how use htmp
* **import** htmp module
```python
import htmp
```

* **init** project
```python
project1 = htmp.Web("<path>", "<directory name>")
```

* **create** html file
```python
page1_htnl = htmp.Html(project1.init("index"))
```

* **load** your project
```python
all_file = [page1_html.source()]
project1.load(all_file)
```
---

### how edit html page
* header Charest
```python
page1_html.Header["charset"]("utf-8")
```

* header title
```python
page1_html.Header["title"]("web site !")
```

* body title (h1, h2, h3, ...)
```python
page1_html.Body["h"](1, "this h1")
#                    ^ is size (1 to 6)
```

* Body text
```python
page1_html.Body["p"]("this text")
```

* Body image
```python
page1_html.Body["img"]("path or url")
```

---

### string shotcut
|Sup|Sub|Bold|italic|Highlight|under-line|center-line|link|
|---|---|----|------|---------|----------|-----------|----|
|^^|^|**|\|#|__|--|:|
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