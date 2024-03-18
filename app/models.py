from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class News(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200,null=True,blank=True),
        description = models.TextField(null=True,blank=True)
    )
    video = models.FileField(upload_to='news/',null=True,blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'News'
    
class Image(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    image = models.FileField(upload_to='news/images/',blank=True, null=True)
    
class Galary(models.Model):
    image = models.ImageField(upload_to="galary",null=True,blank=True) 

class Contact(TranslatableModel):
    translations = TranslatedFields(
        address = models.CharField(max_length=255,null=True,blank=True)
    )
    phone1 = models.CharField(max_length=30,null=True,blank=True)
    phone2 = models.CharField(max_length=30,null=True,blank=True)
    telegram = models.CharField(max_length=200,null=True,blank=True)
    instagram = models.CharField(max_length=200,null=True,blank=True)
    youtube = models.CharField(max_length=200,null=True,blank=True)
    facebook = models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return f"{self.phone1}"

class Vacancy(TranslatableModel):
    translations = TranslatedFields(
        postion = models.CharField(max_length=200,null=True,blank=True),
        specialization = models.CharField(max_length=255,null=True,blank=True),
        education_degree = models.CharField(max_length=200,null=True,blank=True),
        required_experience = models.CharField(max_length=255,null=True,blank=True),
        salary = models.CharField(max_length=255,null=True,blank=True),
        contact = models.CharField(max_length=100,null=True,blank=True)
    )
    date = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Vacancies'

class Service(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200,null=True,blank=True),
        doctor = models.CharField(max_length=200,null=True,blank=True),
        admission = models.CharField(max_length=200,null=True,blank=True),
        description = models.TextField(null=True,blank=True)
    )
    image = models.ImageField(upload_to='services/')
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Services'

class Doctor(TranslatableModel):

    user_type = [
        ('Doctor','Doctor'),
        ('Head','Head')
    ]
    
    user_type = models.CharField(max_length=20,choices=user_type,null=True,blank=True)
    translations = TranslatedFields(
        position = models.CharField(max_length=200,null=True,blank=True),
        name = models.CharField(max_length=250,null=True,blank=True),
        bio = models.TextField(null=True,blank=True),
        admission = models.CharField(max_length=200,null=True,blank=True)
    )
    image = models.ImageField(upload_to='doctors/',null=True,blank=True)
    
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Services'

class AboutUs(TranslatableModel):
    translations = TranslatedFields(
        description = models.TextField()
    )
    image = models.ImageField(upload_to='aboutus/')

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'AboutUs'

class Statistic(models.Model):
    patients = models.IntegerField()
    services = models.IntegerField()
    doctors = models.IntegerField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.patients} | {self.services} | {self.doctors}"
    
class ContactUs(models.Model):
    first_name = models.CharField(max_length=200,null=True,blank=True)    
    last_name = models.CharField(max_length=200,null=True,blank=True) 
    phone = models.CharField(max_length=30,null=True,blank=True)
    date = models.DateField(auto_now_add=True,null=True,blank=True)
    body = models.TextField()

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'ContactUs'
    
    def __str__(self):
        return f"{self.first_name}-{self.last_name}"
    
class Qvp(TranslatableModel):
    translations = TranslatedFields(
        address = models.CharField(max_length=255,null=True,blank=True),
        doctor = models.CharField(max_length=255,null=True,blank=True),
        name = models.CharField(max_length=255,null=True,blank=True),
    )
    image = models.ImageField(upload_to='doctors/',null=True,blank=True)
    contact = models.CharField(max_length=200,null=True,blank=True)