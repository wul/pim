from django.shortcuts import render
from django.views.generic import View
from . import models
# Create your views here.


APP_NAME="portal"

class MemoListView(View):
    def get(self, request):
        return render(request, APP_NAME+'/memo.list.html')
