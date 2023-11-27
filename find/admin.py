from django.contrib import admin
from .models import Post, FindCategory,FindLocation

admin.site.register(Post)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(FindCategory, CategoryAdmin)
admin.site.register(FindLocation, LocationAdmin)