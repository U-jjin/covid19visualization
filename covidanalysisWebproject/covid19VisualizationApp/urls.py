"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from covid19VisualizationApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('gamgi',views.gamgi, name='gamgi'),
    path('gamgis',views.gamgis, name='gamgis'),
    path('gamgi_new',views.gamgi_new, name='gamgi_new'),
    path('gamgi_news',views.gamgi_news, name='gamgi_news'),
    path('chunsik',views.chunsik, name='chunsik'),
    path('chunsiks',views.chunsiks, name='chunsiks'),
    path('openingclosings', views.openingclosings, name='openingclosings'),
]
