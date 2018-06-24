from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'email')
    search_fields = ('username', 'date_joined','email')
    list_per_page = 25


admin.site.register(User,UserAdmin)