from rest_framework import viewsets,permissions,status
from rest_framework.response import Response
from .serializers import *
import json
# Create your views here.

class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return [self.queryset[0]]

class AboutUsView(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        d = request.data
        if not type(d) == type({}):
            d._mutable = True
        d['translations'] = json.loads(request.data.get('translations'))
        serializer = self.get_serializer(data = d)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"message":'created'},status=status.HTTP_200_OK)

    def get_queryset(self):
        return [self.queryset[0]]

class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny,)
    
    def create(self, request, *args, **kwargs):
        d = request.data
        images = request.data.getlist('images')
        if not type(d) == type({}):
            d._mutable = True
        d['translations'] = json.loads(request.data.get('translations'))
        serializer = self.get_serializer(data = d)
        serializer.is_valid(raise_exception = True)
        news = serializer.save()
        for image in images:
            Image.objects.create(news = news, image = image)
        return Response({"message":'created'},status=status.HTTP_200_OK)

class VacancyView(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        d = request.data
        if not type(d) == type({}):
            d._mutable = True
        d['translations'] = json.loads(request.data.get('translations'))
        serializer = self.get_serializer(data = d)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"message":'created'},status=status.HTTP_200_OK)

class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        d = request.data
        if not type(d) == type({}):
            d._mutable = True
        d['translations'] = json.loads(request.data.get('translations'))
        serializer = self.get_serializer(data = d)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"message":'created'},status=status.HTTP_200_OK)

class ContactUsView(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = CuntuctUsSerializer

class QvpView(viewsets.ModelViewSet):
    queryset = Qvp.objects.all()
    serializer_class = QvpSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        d = request.data
        if not type(d) == type({}):
            d._mutable = True
        d['translations'] = json.loads(request.data.get('translations'))
        serializer = self.get_serializer(data = d)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"message":'created'},status=status.HTTP_200_OK)

class StatisticView(viewsets.ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class GalaryView(viewsets.ModelViewSet):
    queryset = Galary.objects.all()
    serializer_class = GalarySerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
