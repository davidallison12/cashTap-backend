from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'bills', views.BillView, 'bill')



urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls))
]