from django.contrib import admin
from .models import Experience
# Register your models here.

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'category', 'started_at', 'ended_at')
    list_filter = ('category',)
    search_fields = ('title', 'organization', 'description')
