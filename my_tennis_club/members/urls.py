from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.main, name='main'),
    path('member_list/', views.member_list, name='member_list'),
    path('detail/<int:pk>/', views.details, name='detail'),
]
