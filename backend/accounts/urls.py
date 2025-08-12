from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterView, UserProfileView, ChangePasswordView, LogoutView, UserStatsView, CustomLoginView, CheckAuthView

urlpatterns = [
    # Authentication endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('check-auth/', CheckAuthView.as_view(), name='check_auth'),
    
    # User profile endpoints
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    
    # Admin endpoints
    path('stats/', UserStatsView.as_view(), name='user_stats'),
]