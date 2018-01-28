"""pim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from . import views
app_name = "api"
urlpatterns = [
    path('catalog/', views.CatalogListView.as_view(), name="catalog-list"),
    re_path('catalog/(?P<pk>\d+)/', views.CatalogDetailView.as_view(), name="catalog"),        
    path('memo/', views.MemoListView.as_view(), name="memo-list"),
    re_path('memo/(?P<pk>\d+)/', views.MemoDetailView.as_view(), name="memo"),    
]
