from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from polls.models import Manufacture, Car
from polls.models import DRAFT_CHOICES


@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    search_fields = ('id', 'name')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'color', 'status',)
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('name', 'manufacture', 'date', 'color',)
