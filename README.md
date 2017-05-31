# mysite
test site for django, html, css, javascript

- [ ] asdf
- [X] asfd

**1. create a Django app called newapp:**
```bash
cd into project/
python manage.py startapp newapp
```

**2. add newapp to INSTALLED_APPS in project/project/settings.py**

**3. create urls.py in newapp with the following content:**
```python
# newapp/urls.py
from django.conf.urls import url
from newapp import views

urlpatterns = [
  url(r'^$', views.HomePageView.as_view()),
]
```

**4. add newapp's urls to project in project/project/urls.py in urlpattern:**
```python
  url(r'^', include('newapp.urls')),
```

**5. add basic content to newapp/views:**
```python
from django.views.generic import TemplateView

class HomePageView(TemplateView):
  def get(self, request, **kwargs):
    return render(request, 'index.html', context=None)
```

**6. create templates folder in newapp.**
```bash
mkdir project/newapp/templates

```
**7. create index.html in templates folder with the following basic content:**
```bash
touch project/newapp/templates/index.html
```
```html
<!-- newapp/templates/index.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>NewApp!</title>
  </head>
  <body>
    <h1>Howdy! I am Learning Django!</h1>
  </body>
</html>
```
