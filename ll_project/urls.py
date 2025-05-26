"""
URL configuration for ll_project project.

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
from django.contrib import admin #lets you use admin interface.
#include() for accessing the urls file in learning_logs folder.
from django.urls import path, include #path() used to map urls to view fns

#contains the urls from the apps in the project.
urlpatterns = [
    path('admin/', admin.site.urls), #all urls that can be requested from the admin site.
    path('accounts/', include('accounts.urls')),
    path('', include('learning_logs.urls')),
]
