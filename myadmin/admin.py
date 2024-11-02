from django.contrib import admin
from .models import Hero, AboutMe, Skill, Logo, Service, MyWork, Contact
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.utils.html import format_html





def index(self, request, extra_context=None):
        response = super().index(request, extra_context=extra_context)
        response.context_data['site_url'] = settings.SITE_URL  # Set the SITE_URL to the custom URL
        return response

# Instantiate the custom admin site




@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo_image', 'created_at', 'updated_at')

    # Prevent adding a new Logo if one already exists
    def has_add_permission(self, request):
        if Logo.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    # Customize the way the logo image is displayed in the admin
    def logo_image(self, obj):
        if obj.logo_image:
            return format_html(
                '<img src="{}" style="width: 130px; height: 68px; object-fit: cover;" />',
                obj.logo_image.url
            )
        return "No image"
    logo_image.short_description = "Logo"



@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'small_description', 'created_at', 'updated_at')
    search_fields = ('full_name', 'small_description')
    list_filter = ('created_at', 'updated_at')

    # Prevent adding a new Hero if one already exists
    def has_add_permission(self, request):
        if Hero.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('about_me_para1', 'about_me_para2', 'years_of_experience', 'projects', 'happy_clients', 'created_at', 'updated_at')

    # Prevent adding a new AboutMe if one already exists
    def has_add_permission(self, request):
        if AboutMe.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'created_at', 'updated_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('numro_service', 'service_name', 'service_description', 'created_at', 'updated_at')


@admin.register(MyWork)
class MyWorkAdmin(admin.ModelAdmin):
    list_display = ('project_imagee', 'project_url', 'created_at', 'updated_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_para', 'phone_number', 'localisation', 'email', 'created_at', 'updated_at')

    # Prevent adding a new Contact if one already exists
    def has_add_permission(self, request):
        if Contact.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
