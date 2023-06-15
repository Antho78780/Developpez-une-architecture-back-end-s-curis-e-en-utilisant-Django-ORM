from django.urls import path, include
from authentication import views
from rest_framework import routers

app_name = 'authentication'

router = routers.DefaultRouter()
router.register(r'register', views.Register, basename='register')
router.register(r'login', views.Login, basename='login')

urlpatterns = [
    path('auth/', include(router.urls))
]