from django.contrib import admin
from .models import Brand, Motorcycle, MotorcycleImage, Specification

class MotorcycleImageInline(admin.TabularInline):
    model = MotorcycleImage
    extra = 3

class SpecificationInline(admin.StackedInline):
    model = Specification

@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'motorcycle_type', 'price']
    list_filter = ['brand', 'motorcycle_type', 'year']
    search_fields = ['brand__name', 'model']
    inlines = [SpecificationInline, MotorcycleImageInline]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'founded']

admin.site.register(Specification)
