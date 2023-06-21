from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('lg', views.list_game),
    path('wiki', views.wiki),
    path('forms', views.forms),

]
