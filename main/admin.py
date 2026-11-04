from django.contrib import admin
from .models import Experience, Interest, Project
# Register your models here.

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'category', 'started_at', 'ended_at')
    list_filter = ('category',)
    search_fields = ('title', 'organization', 'description')

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill')
    search_fields = ('title', 'skill')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'project_url')
    search_fields = ('title', 'tech_stack', 'description')
