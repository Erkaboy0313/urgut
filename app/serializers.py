from rest_framework import serializers
from . models import AboutUs,ContactUs,News,Contact,Vacancy,Service,Doctor,Statistic,Qvp,Galary,Image
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from . mixins import TranslatedSerializerMixin

class AboutUsSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = AboutUs)
    class Meta:
        model = AboutUs
        fields = "__all__" 

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class NewsSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = News)
    image_set = ImageSerializer(many = True,read_only = True)
    class Meta:
        model = News
        fields = "__all__" 

class ContactSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = Contact)
    class Meta:
        model = Contact
        fields = "__all__" 
    
class VacancySerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = Vacancy)
    class Meta:
        model = Vacancy
        fields = "__all__" 

class ServiceSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = Service)
    class Meta:
        model = Service
        fields = "__all__" 

class DoctorSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = Doctor)
    class Meta:
        model = Doctor
        fields = "__all__"

class QvpSerializer(TranslatedSerializerMixin,TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = Qvp)
    class Meta:
        model = Qvp
        fields = "__all__"

class GalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Galary
        fields = '__all__'
           
class CuntuctUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"

class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = "__all__"