from django.urls import path
from .views import home
from .views import home1
urlpatterns = [
    path('',home,name='home'),
    path('a/<int:id>/',home1, name='a')
]