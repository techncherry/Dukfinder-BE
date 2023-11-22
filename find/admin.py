from django.contrib import admin
from .models import FindPost, FindCategory, FindComment

admin.site.register(FindPost)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(FindCategory, CategoryAdmin)
admin.site.register(FindComment)