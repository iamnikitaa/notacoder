from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    
    # User signs in here
    path('sign-in/', views.choose_access, name='choose_access'),
    
    # Once signed in, they see list of challenges
    path('challenges/', views.challenge_list, name='challenge_list'),
    
    # --- THIS IS THE ONLY URL YOU NEED FOR A SPECIFIC CHALLENGE ---
    # Detailed view for a single challenge. This is what we will redirect to.
    path('challenges/<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
    
    # Optional entry point or intro to challenges
    path('challenge-entry/', views.challenge_entry, name='challenge_entry'),

    path('dashboard/', views.user_dashboard, name='user_dashboard'),

    # --- DELETE THE LINE BELOW ---
    # path('challenge/<int:challenge_number>/', views.challenge_page_view, name='challenge_page'), # REMOVED
]

