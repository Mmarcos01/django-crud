from django.shortcuts import render
from .models import Snack
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


class SnackListView(ListView):
    pass
class SnackDetailView(DetailView):
    pass
class SnackCreateView(CreateView):
    pass
class SnackUpdateView(UpdateView):
    pass
class SnackDeleteView(DeleteView):
    pass



# Create SnackListView that extends appropriate generic view
# associated url path is an empty string
# Create SnackDetailView that extends appropriate generic view
# associated url path is <int:pk>/
# Create SnackCreateView that extends appropriate generic view
# associated url path is create/
# Create SnackUpdateView that extends appropriate generic view
# associated url path is <int:pk>/update/
# Create SnackDeleteView that extends appropriate generic view
# associated url path is <int:pk>/delete/
