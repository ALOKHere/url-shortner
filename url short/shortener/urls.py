from django.urls import path
from .views import HomeView, redirect_url, RegisterView

app_name = 'shortener'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),  # ✅ This must be here
    path('<str:code>/', redirect_url, name='redirect'),
]
