from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('redirect-page', views.redirect_method),
]