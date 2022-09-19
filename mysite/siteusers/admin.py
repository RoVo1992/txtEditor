from django.contrib import admin

# Register your models here.
from .models import *


class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(SiteUser, SiteUserAdmin)
