from rest_framework.routers import DefaultRouter,SimpleRouter
from django.conf import settings
from .views import LoginView,SecurityView

if settings.DEBUG:
    auth_router = DefaultRouter()
else:
    auth_router = SimpleRouter()

auth_router.register(r'login',LoginView,basename="login")
auth_router.register(r'security',SecurityView,basename="security")