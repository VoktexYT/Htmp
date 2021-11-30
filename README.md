# H T M P

---
---
* **how install and config**
* **how use htmp**
* **how edit html code** 
* **string shortcut**
* **credit**
---
---

### how install and config
* For install module, click on green button "code" and download
* To use the module, choose the htmp manager and place it in your project
* To try, import it into your python file

---

### how use htmp
* install htmp module
```python
import htmp
```

* init project
```python
project1 = htmp.Web("<path>", "<directory name>")
```

* create html file
```python
page1_htnl = htmp.Html(project1.init("index"))
```

* load your project
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
