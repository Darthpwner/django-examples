from django.contrib import admin

from django_server import models


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
