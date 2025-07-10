from django.contrib import admin
from .models import Home, About, profile, Category, skills, Portfolio
# Register your models here.

    #Home 
admin.site.register(Home)

# About
class ProfileInline(admin.TabularInline):
    model = profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]
# Skills
class SkillsInline(admin.TabularInline):
    model = skills
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines =[
        SkillsInline,
    ]

#portfolio
admin.site.register(Portfolio)