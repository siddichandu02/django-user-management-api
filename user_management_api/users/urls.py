from django.urls import path
from .views import SignupView, SigninView, ProfileView, UpdateCredentialsView, UserSearchView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update-credentials/', UpdateCredentialsView.as_view(), name='update-credentials'),
    path('search/', UserSearchView.as_view(), name='user-search'),
]
