![logo](https://github.com/idoyudha/visit_komodo/blob/master/visit_komodo/static/images/logo.png?raw=true)
# VISIT_KOMODO
Komodo Island is an island blessed with many wonderful things with amazing scenery. The special one is Komodo National Park with three major island Rinca, Padar, and Komodo, and is home to approximately 2,500 Komodo Dragons and other terrestrial fauna such as various species of reptiles, birds, and mammals. With many exciting things that we explained earlier, until now Komodo national park still not easy to get the detailed information about that and make us a little bit difficult to prepare to explore.

So, this web application help users discover the beauty of Komodo Island for a better experience. Discover where they want to go, planning for the next event, what to eat and what needs to prepared. Users also can book flights directly from the detail page with the help of the Skyscanner travel widget.

# Project requirements and demonstration
The detail of project specifications are listed [here](https://cs50.harvard.edu/web/2020/projects/final/capstone/). And the [demonstration](https://youtu.be/jRy9C27-Ma8).

## Distinctiveness
On the profile page, users could see their contributions that have written. Using navbar for every submenu, so users can click on it and it will show without rendering the page.

The visit komodo web applications aim to provide and share information about destinations, food, event, and travel guide. Special for a travel guide, in this section users, can write using a rich text editor for more powerful writing more than simple markdown text.

Django, CSS, Javascript, and other libraries will make this website easy to maintain and deliver data to the front end using API. And provide a more attractive user experience.

## Responsiveness
This web app utilizes CSS and Bootstrap library to provide responsive design. The layout adapts to the screen size when the browser window is minimized or viewed on the mobile device.
![alt text](https://github.com/idoyudha/visit_komodo/blob/master/visit_komodo/static/readme-media/responsive.gif?raw=true)

## Project implementation 
The web application utilizes Django with a combination feature Django REST framework for building web APIs and Django CKEditor that provides a ``RichTextField``, ``RichTextUploadingField``, ``CKEditorWidget`` and ``CKEditorUploadingWidget`` utilizing CKEditor with image uploading and browsing support included.

The Django project name is final_project and has a single app named visit_komodo.

Javascript with the combination of the Bootstrap library is utilized in the frontend for website responsiveness. The javascript function is made specifically the use of APIs from the Django REST framework, so the information is delivered without reloading the page every time the user makes a request.

# Website feature and complexity

## Multi-page application
This web app is a multi page-application. The main feature is in the profile page which users can request the contribution that they write, editing their profile, and link for writing blog. The result will be showing on the front or landing page.

## Landing page and submenu
![landing page](https://github.com/idoyudha/visit_komodo/blob/master/visit_komodo/static/readme-media/landing_page.gif?raw=true)

The layout is designed for a better user experience special for travelers. With wide image separation between destination, food, and events, and travel guide. 

![submenu](https://github.com/idoyudha/visit_komodo/blob/master/visit_komodo/static/readme-media/submenu.gif?raw=true)

No need to log in if the users just want to see the page and detail for every page.

## Detail page
On this page, users can read the description of the title and add it to their wishlist. Also, this page provides a Skyscanner travel widget for flight, users can type directly on this page, where they want to go. Not just that, users also edit or delete this page if this page is written by themself.
![detail page](https://github.com/idoyudha/visit_komodo/blob/master/visit_komodo/static/readme-media/detail_page.gif?raw=true)

## User registration and login
![register](https://github.com/idoyudha/visit_komodo/blob/master/visit_komodo/static/readme-media/register.png?raw=true)
![login](https://github.com/idoyudha/visit_komodo/blob/master/visit_komodo/static/readme-media/login.png?raw=true)
If users want to write and add to their wishlist, they need to register first. Or log in if they already have the account.

## Profile page
The main feature is on this page. Where users can edit their default profile using button modal, request their list of contributions of destination, event, food, and travel guide. And there are two buttons for write a listing (destination, event, and food) and a button for writing a blog with a special feature of rich text editor.

![profile page](https://github.com/idoyudha/visit_komodo/blob/master/visit_komodo/static/readme-media/profile_page.gif?raw=true)

## Write blog
This page comes with the special feature of rich text editor for a better writing experience. This feature has output special for travel guides that need more descriptive words.
![add blog](https://github.com/idoyudha/visit_komodo/blob/master/visit_komodo/static/readme-media/add_blog.gif?raw=true)
![blog page](https://github.com/idoyudha/visit_komodo/blob/master/visit_komodo/static/readme-media/blog_page.gif?raw=true)

## Wishlist
Users can see their wishlist on this page when clicking your image profile in the navbar, it will show a dropdown to profile and wishlist. Almost the same as the profile page, on this page users can request their wishlist without reloading the page.

![wishlist](https://github.com/idoyudha/visit_komodo/blob/master/visit_komodo/static/readme-media/wishlist.gif?raw=true)

## Feature conclusion
- Build with [Django Web framework](https://www.djangoproject.com/), it allows us to build and serialize JSON object to URL that has been provided. Django REST framework is a powerful and flexible toolkit for building Web APIs.
- Write a blog using a rich text editor, it allows us to write a blog with many expressions in our head, more than a simple text field. We can add an image with a URL, perform space and enter, **bold** and _italic_ the text. Simply like markdown text in the template. Build with [Django CKEditor](https://github.com/django-ckeditor/django-ckeditor).
- Users can add to their wishlist place, food, or event.
- Simply can search flight to destination directly from the detail page, with the Skyscanner widget.
- Users can edit their profile right after registration, replace the default value.
- It's mobile responsive, support by [Bootstrap](https://getbootstrap.com/) library with the latest version.
- After all, users can Create, Read, Update, and Delete what users write on the web.

# Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
- [Python programming language](https://www.python.org/about/).
- [Django Web framework](https://www.djangoproject.com/) has been installed on your local machine. Click this link about how to get [django](https://www.djangoproject.com/download/).

## Install dependant
Install all dependat packages in requirements.txt including Django REST Framework and Django CKEditor.
```
$ pip3 install -r requirements.txt
```

## Initialize database
Install all dependat packages in requirements.txt including Django REST Framework and Django CKEditor
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
Create superuser
```
$ python3 manage.py createsuperuser
```

## Starting server
To start the server on your local machine, first, go to the manage.py directory in your app and run the following commands:
```
$ python3 manage.py runserver
```
You’ll see the following output on the command line:
```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

January 1, 2021 - 5:50:53
Django version 3.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

# Project File

## setting.py
Setting the following lines into the  ``INSTALLED_APPS``
```
INSTALLED_APPS = [
    'visit_komodo.apps.VisitKomodoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'ckeditor',
    'rest_framework',
]
```
## admin.py
Write the registered model in this file, so admin can manage in their interface. Look below for registering users model just for example.
```
admin.site.register(User)
```

## urls.py
Contains the URL patterns used by the web application, including URL APIs.
```
urlpatterns = [
  ...
]
```

## forms.py
Define a form for the blog models which is used for writing the travel guide.
```
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    class Meta:
        content = forms.CharField(widget=CKEditorWidget())
        model = Blog
        fields = ['title', 'short_description', 'image_url', 'body']
```

## serializers.py
The file has a function to make a JSON serializer from the model output. Below is just an example.
```
from rest_framework import serializers

from .models import Destination

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination 
        fields = '__all__'
```

## views.py
Write functionality to process the user request.
_Imported packages_
```
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Django REST Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
```
**_@login_required decorator_**

Paths that require that the user is authenticated will have the login_required decorator. Will redirect to the login page if user makes a request to this view.

**_@csrf_exempt_**

The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their browser. [CSRF](https://docs.djangoproject.com/en/3.1/ref/csrf/)

## index.js
This javascript file includes all functions to get JSON data from APIs URL like add to wishlist and fetch data for getting all list of wishlist and contribution. All done without reloading the page.

Additional function like csrf token required for AJAX POST Rrequest data through fetching. We can acquire the token like this:
```
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
```

## layout.html
The main template for all that contains the navbar and footer that will appear on all of the pages. All HTML pages will include this line on the top.
```
{% extends "visit_komodo/layout.html" %}
```
This layout.html must include the framework that comes from CDN, like bootstrap. Also include the script tag ``index.js``from the static folder.
```
<!-- Bootstrap CDN -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.cssrel="stylesheet" ...">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.0/fonbootstrap-icons.css">

<!-- Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" ..."></script>
<script type="text/javascript" src="{% static 'js/index.js' %}"></scrip
```

## styles.css
This CSS file contains all style setting for better user experience, including export fonts from googleapis.
```
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
```

# Architecture
## Frontend
- Languages:
  - HTML
  - CSS
  - JavaScript
- Main framework/libraries:
  - [Django template language](https://docs.djangoproject.com/en/3.1/ref/templates/language/)
  - [Bootstrap](https://getbootstrap.com/)
  - [Skyscanner travel widget](https://www.partners.skyscanner.net/affiliates/widgets-quick-start)
  - [Google font](https://fonts.google.com/)

## Backend 
- Language:
  - [Python](https://www.python.org/)
- Main framework/libraries:
  - [Django Web framework](https://www.djangoproject.com/)
  - [Django REST framework](https://www.django-rest-framework.org/)
  - [Django CKEditor](https://github.com/django-ckeditor/django-ckeditor)
  
**Databases**
- [SQLite](https://www.sqlite.org/index.html)

## Author
- **Ido Widya Yudhatama** - _Initial work_

## Bug Reports and Improvements
If you experience any bugs or anything that can be improved, please feel free to open an issue [here](https://github.com/idoyudha/commerce/issues) or simply contact me through any of the links below. Thank you in advance!
- Email: idowidya.yudhatama@gmail.com
- [LinkedIn](https://www.linkedin.com/in/idoyudha/)
