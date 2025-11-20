from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.member_list, name='list'),
    path('detail/<int:pk>/', views.details, name='detail'),
]
