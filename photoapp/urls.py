from django.urls import path
from django.urls import path
from photoapp import views	
urlpatterns = [
    path("", views.home, name="home"),
]

