from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    )
from .views import MyTokenObtainPairView, UserCreateView

router = routers.DefaultRouter()
router.register(r'bills', views.BillView, 'bill')
router.register(r'users', views.UserCreateView, 'user')
router.register(r'profiles', views.ProfileView, 'profile')


urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/register/',include(UserCreateView)
    path('api/register/', UserCreateView.as_view(), name='register')
]