from django.contrib import admin
from .models import *

from parler.admin import TranslatableAdmin

admin.site.register(ContactUs)
admin.site.register(Statistic)
admin.site.register(Image)

@admin.register(News)
class AboutUsAdmin(TranslatableAdmin):
    list_display = ('title',)

@admin.register(Contact)
class AboutUsAdmin(TranslatableAdmin):
    list_display = ('phone1','phone2')

@admin.register(Vacancy)
class AboutUsAdmin(TranslatableAdmin):
    list_display = ('postion',)

@admin.register(Service)
class AboutUsAdmin(TranslatableAdmin):
    list_display = ('name',)

@admin.register(Doctor)
class AboutUsAdmin(TranslatableAdmin):
    list_display = ('name',)

@admin.register(AboutUs)
class AboutUsAdmin(TranslatableAdmin):
    list_display = ('description',)

@admin.register(Qvp)
class QvpAdmin(TranslatableAdmin):
    list_display = ('address',)

admin.site.register(Galary)
