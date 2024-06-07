from django.contrib import admin
from apps.users import models
# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'age', 'direction', 'balance', 'wallet')
    list_filter = ('username', 'phone', 'age', 'direction', 'balance', 'wallet')
