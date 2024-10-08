"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dbms.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",landing, name="landing"),
    path("login", login, name = "login"),
    path("insert", insert_data, name = "insert"),
    path("save", saved, name = "saved"),
    path("display", display, name = "display"),
    path("display2/", display2, name="display2"),
    path("update/<id>", update, name = "update"),
    path("delete/<id>", delete_data, name = "delete"),
]
