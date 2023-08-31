from django.urls import path
from .views import *


urlpatterns = [
    path('search/', SearchUserView.as_view(), name="user-search"),    
    path('all/', GetUserView.as_view(), name="users"),    
    path('<int:id>/', GetUserDetailView.as_view(), name="user-details"),    
]
