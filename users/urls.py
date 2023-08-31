from django.urls import path
from .views import *


urlpatterns = [
    path('all/', GetUserView.as_view(), name="users"),    
]
