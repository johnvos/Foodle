from django.urls import path
from profilepage import views

urlpatterns = [
    path('', views.profile, name='profile')
]
