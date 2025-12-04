from firstapp import views
from django.urls import path

urlpatterns = [
    path("home/",views.home),
    path("morning/",views.good_morning),
    path("evening/",views.good_evening),
    path("night/",views.good_night),
]
