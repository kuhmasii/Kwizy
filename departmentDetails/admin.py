from django.contrib import admin
from .models import Level

class LevelAdmin(admin.ModelAdmin):
    list_display = ("name", "slug_name")
    list_filter = ("name",)
    prepopulated_fields = {"slug_name": ("name",)}

admin.site.register(Level, LevelAdmin)
