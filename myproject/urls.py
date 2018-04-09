"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import myapp.views as views
from django.urls import path
from myapp.views import printStudent
from myapp.views import sectionStudent

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', views.hello),
    url(r'^refresh/', views.language),
    url(r'^thanks/', views.hello),
    url(r'^your-name/', views.get_name),
    url(r'^students/', printStudent.as_view()),
    path('section/<section>/', sectionStudent.as_view()),
    url(r'^video', views.HomeView.as_view(), ),
    url(r'^embedvideo', views.embedVideo),
]
