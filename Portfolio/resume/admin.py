from django.contrib import admin
from .models import *
# Register your models here.


class EducationAdmin(admin.ModelAdmin):
    list_display = ['university_name', 'start_date', 'end_date', 'grade']
    list_filter = ['start_date']
    search_fields = ['university_name']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'start_date', 'end_date', 'activity']
    list_filter = ['company']
    search_fields = ['company', 'activity']


class InitialsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_surname']
    list_filter = ['first_name']
    search_fields = ['first_name']


class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['language', 'level']
    list_filter = ['language']
    search_fields = ['language']


class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ['linkname']


admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Infos)
admin.site.register(Initials)
admin.site.register(For_clients)
admin.site.register(Summery)
admin.site.register(Experience)
admin.site.register(Header)
admin.site.register(Services)
admin.site.register(Stuff)
admin.site.register(Count_Box)
admin.site.register(PersonalInfo)
admin.site.register(Message)
admin.site.register(SocialLinks)
admin.site.register(PortfolioProject)
admin.site.register(Languages)
admin.site.register(Courses)