from django.contrib import admin
from .models import Driver_Details


class Driver_DetailsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Phone_Number')


admin.site.register(Driver_Details, Driver_DetailsAdmin)


