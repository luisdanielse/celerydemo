from django.contrib import admin
from .models import periodicMessage

class periodicMessageAdmin(admin.ModelAdmin):
    list_display = ['message',
                    'creacion']

# Register your models here.
admin.site.register(periodicMessage,periodicMessageAdmin)
