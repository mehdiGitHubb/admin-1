from django.db import models
from django.core.exceptions import ValidationError
import os

def validate_image_or_svg(value):
    ext = os.path.splitext(value.name)[1]  # Get file extension
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions are: .jpg, .jpeg, .png, .gif, .svg')

class Hero(models.Model):
    full_name = models.CharField(max_length=255)
    small_description = models.CharField(max_length=255)
    description = models.TextField()
    
    profile_image = models.FileField(upload_to='profile_images/', validators=[validate_image_or_svg])  # Custom validator for SVG and other image types
    cv = models.FileField(upload_to='cvs/')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name




class AboutMe(models.Model):
    about_me_para1 = models.TextField()  # First paragraph about yourself
    about_me_para2 = models.TextField()  # Second paragraph about yourself
    about_me_image = models.FileField(upload_to='about_me_images/', null=True, blank=True,  validators=[validate_image_or_svg])  # Custom validator for SVG and other image types
    years_of_experience = models.PositiveIntegerField()  # Years of experience
    projects = models.PositiveIntegerField()  # Number of projects
    happy_clients = models.PositiveIntegerField()  # Number of happy clients
    created_at = models.DateTimeField(auto_now_add=True)  # Date created
    updated_at = models.DateTimeField(auto_now=True)  # Date updated

    def __str__(self):
        return f"{self.years_of_experience} years of experience"


class Skill(models.Model):
    name = models.CharField(max_length=255)  # Name of the skill
    percentage = models.PositiveIntegerField()  # Skill proficiency percentage (0-100)
    created_at = models.DateTimeField(auto_now_add=True)  # Date created
    updated_at = models.DateTimeField(auto_now=True)  # Date updated
    def __str__(self):
        return self.name

class Logo(models.Model):
    logo_image = models.FileField(upload_to='logo_images/', validators=[validate_image_or_svg])  # Custom validator for SVG and other image types
    created_at = models.DateTimeField(auto_now_add=True)  # Date created
    updated_at = models.DateTimeField(auto_now=True)  # Date updated
    def __str__(self):
        return f"{self.id} id"
    


class Service(models.Model):
    numro_service = models.IntegerField(unique=True)  # Unique number for each service
    service_name = models.CharField(max_length=255)   # Name of the service
    service_description = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  # Date created
    updated_at = models.DateTimeField(auto_now=True)  # Date updated          # Description of the service

    def __str__(self):
        return self.service_name
    


class MyWork(models.Model):
    project_imagee = models.FileField(upload_to='projects/', null=True, validators=[validate_image_or_svg])  # Custom validator for SVG and other image types
    project_url = models.URLField(max_length=200)  # URL field for project links
    created_at = models.DateTimeField(auto_now_add=True)  # Date created
    updated_at = models.DateTimeField(auto_now=True)  # Date updated  

    def __str__(self):
        return f"Project: {self.project_url}"
    



class Contact(models.Model):
    contact_para = models.TextField(verbose_name="Contact Paragraph")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    localisation = models.CharField(max_length=255, verbose_name="Localisation")
    email = models.EmailField(max_length=255, verbose_name="Email Address")
    created_at = models.DateTimeField(auto_now_add=True)  # Date created
    updated_at = models.DateTimeField(auto_now=True)  # Date updated 
    def __str__(self):
        return f"Contact Info - {self.email}"



