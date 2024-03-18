from rest_framework.routers import DefaultRouter,SimpleRouter
from django.conf import settings
from .views import ContactView,AboutUsView,NewsView,VacancyView,ServiceView,DoctorView,ContactUsView,StatisticView,QvpView,GalaryView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r'contact',ContactView,basename='contact')
router.register(r'about',AboutUsView,basename='about')
router.register(r'news',NewsView,basename='news')
router.register(r'vacancy',VacancyView,basename='vacancy')
router.register(r'service',ServiceView,basename='service')
router.register(r'doctor',DoctorView,basename='doctor')
router.register(r'contactus',ContactUsView,basename='contactus')
router.register(r'home',StatisticView,basename='home')
router.register(r'qvp',QvpView,basename='qvp')
router.register(r'galary',GalaryView,basename='galary')
