# Django_rest_api

## Requirements
- Python 3.5+
- Django 2.2+
- Django REST Framework 3.11+


## How to install

- $ pip install djangorestframework

<u> Creation of project and app </u>

- $ django-admin startproject djano_rest_api
- $ cd djano_rest_api
- $ python manage.py startapp src
<hr>

## Run Django application
- Check requirements and install the required modules and api.
```
$ python manage.py runserver
```


## API : Application Programming Interface
```API
An application program interface (API) is a set of routines, protocols, and tools for building
software applications. An application programming interface (API) is a computing interface to a
software component or a system, that defines how other components or systems can use it. It 
defines the kinds of calls or requests that can be made, how to make them, the data formats that
should be used, the conventions to follow, etc. It can also provide extension  mechanisms so that
users can extend existing functionality in various ways and to varying degrees. An API can be
entirely custom, specific to a component, or it can be designed based on an industry standard to
ensure interoperability. 
```
## Source: [Wikipedia API](https://en.wikipedia.org/wiki/Application_programming_interface)

## REST Framework
- It describe an architecture which stands for Representational State Transfer.
- Django REST framework is a powerful and flexible toolkit for building Web APIs.

```Intro
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application 
using the HTTP methods:
GET, POST, PUT, DELETE. Endpoints should be logically organized around collections and elements, 
both of which are resources. In our case, we have one single resource, posts, 
so we will use the following URLS - /posts/ and /posts/<id> for collections and elements, respectively.
```

<hr>

|        | GET  | POST | PUT | Delete |
| ------ | ------------- | ------------- | --------| --------|
| /posts/ | Show all posts | Add new post | Update all posts | Delete all posts |
| /posts/\<id> | Show \<id>  | N/A  | 	Update \<id> | Delete \<id> |

- GET is used to retrieve a resource 
- PUT is used to change the state or update a resource which can be a file or block.
- POST is used to create the resource.
- DELETE is used to delete or remove that resource.
<hr>

## What is REST Api?

```api
When web services use REST architecture, they are called RESTful APIs or REST APIs.
A REST API is a set of web addresses that responds with pure information, not a formatted web page.
An API returns a JSON, which is common format.

```

## Model Serializer
```serializer
DRF’s Serializers convert model instances to Python dictionaires, which can then be rendered in
 various API appropriate formats - like JSON or XML. Similar to the Django ModelForm class, DRF 
comes with a concise format for its Serializers, the ModelSerializer class. It’s simple to use.
```

```Python```
```
from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
#       fields = ('firstname', 'lastname')
=> Save this as serializers.py within the “src” directory.

```


