"""
URL configuration for MerconExport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from me_project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('carpet_pg/', views.carpet_pg, name="carpet_pg"),
    path('furniture_pg/', views.furniture_pg, name="furniture_pg"),
    path('jute_pg/', views.jute_pg, name="jute_pg"),
    path('leather_pg/', views.leather_pg, name="leather_pg"),
    path('marble_pg/', views.marble_pg, name="marble_pg"),
    path('textile_pg/', views.textile_pg, name="textile_pg"),
]
