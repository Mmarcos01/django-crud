from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView 

urlpatterns = [
    path('', SnackListView.as_view(), name="list_view"),
    path('<int: pk>', SnackDetailView.as_view(), name="detail_view"),
    path('', SnackCreateView.as_view(), name="create_view"),
    path('', SnackUpdateView.as_view(), name="update_view"),
    path('', SnackDeleteView.as_view(), name="delete_view"),
] 


