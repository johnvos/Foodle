from django.urls import path
from restaurantpage import views

urlpatterns = [
    path('', views.showpage, name='showpage')
]
