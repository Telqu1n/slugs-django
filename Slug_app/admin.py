from django.contrib import admin
from .models import Food

# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}