from django.urls import path,include
from django.conf import settings
from . import views
urlpatterns=[
    path("login/",views.login,name = "login"),
    path("convertor/",views.convertor,name = "convertor"),
]