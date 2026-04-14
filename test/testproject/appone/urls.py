from django.urls import path
from appone.views import home


urlpatterns = [
    path('', home, name='home'),
]
