from django.urls import path, include
from rest_framework import routers
from contract import views

app_name = 'contract'

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet, basename='customers')
router.register(r'contract', views.ContractViewSet, basename='contract')
router.register(r'event', views.EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls))
]