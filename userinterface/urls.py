from django.urls import path
from userinterface import views as VIEWS


urlpatterns = [
    path('', VIEWS.home, name='home'),
]
