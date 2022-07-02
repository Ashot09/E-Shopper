from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import HomeBG

# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homebg = HomeBG.objects.all()
        return render(request, self.template_name, {'homebg':homebg})