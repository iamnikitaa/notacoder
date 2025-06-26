from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sign-in/', views.login_view, name='login'),

    path('challenges/', views.challenge_list, name='challenge_list'),
    path('challenges/<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
    path('challenge-entry/', views.challenge_entry, name='challenge_entry'),
]

