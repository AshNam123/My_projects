from django.urls import path
from . import views


#create path

urlpatterns = [
    path('',views.index,name = "index"),
]
