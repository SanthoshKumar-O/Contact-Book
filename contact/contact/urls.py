"""
URL configuration for contact project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from application import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.contactbook,name="contactbook"),
    path('home/',views.home,name="home"),
    path('list/',views.listcontact,name="List_contact"),
    path('delete/<int:id>/',views.deletecontact,name="delete_contact"),
    path('search/',views.searchcontact,name="search_contact"),
    path('update/<int:id>/',views.updatecontact,name="update_contact"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.loginview,name="login"),
    path('logout/',views.logoutview,name='logout'),
    path('',views.frontpage,name="welcome"),
]
