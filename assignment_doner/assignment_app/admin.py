from django.contrib import admin
from .models import User_data, App_content

# Register your models here.
admin.site.register(User_data)
@admin.register(App_content)
class AppContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')