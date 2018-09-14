"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from to_do_list_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_render, name='list_render'),
    path('save_list_object', views.save_list_object, name='save_list_object'),
    path('archive_list_object/', views.archive_list_object, name='archive_list_object'),
    path('delete_list_object/', views.delete_list_object, name='delete_list_object'),
]
