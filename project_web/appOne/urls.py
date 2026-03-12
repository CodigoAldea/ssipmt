from django.urls import path
from appOne.views import home, profile

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
]