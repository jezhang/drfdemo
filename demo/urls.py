
from django.urls import path

from demo import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),

]
