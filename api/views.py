from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import serializer
from portal import models
# Create your views here.


class CatalogListView(ListCreateAPIView):
    queryset = models.Catalog.objects.all()
    serializer_class = serializer.CatalogSerializer    

class CatalogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Catalog.objects.all()
    serializer_class = serializer.CatalogSerializer

class MemoListView(ListCreateAPIView):
    queryset = models.Memo.objects.all()
    serializer_class = serializer.MemoSerializer    

class MemoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Memo.objects.all()
    serializer_class = serializer.MemoSerializer    
