from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
class home(TemplateView):
    template_name='app/home.html'
    
class School_List(ListView):
    model=School
    context_object_name='schl'


class School_Detail(DetailView):
    model=School
    context_object_name='schobj'

class School_Create(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='Schobject'
    success_url=reverse_lazy('School_List')