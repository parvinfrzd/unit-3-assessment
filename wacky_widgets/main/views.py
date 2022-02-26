from ast import Delete
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import  DeleteView
from .forms import WidgetForm

from .models import Widget

def home(request):
    widgets = Widget.objects.all()
    form = WidgetForm(request.POST)
    if form.is_valid():
        widget = form.save(commit=False)
        widget.save()
        return redirect('/')
        
    return render(request, 'home.html', {'widgets': widgets, 'form': form}) 

class WidgetDelete(DeleteView): 
    model = Widget
    success_url = '/'