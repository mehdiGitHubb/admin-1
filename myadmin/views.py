from django.http import JsonResponse
from .models import Hero
from .models import AboutMe
from .models import Skill
from .models import Logo
from .models import Service
from .models import MyWork
from .models import Contact






def get_hero(request):
    hero = Hero.objects.first()  # Assuming you have only one hero entry
    if hero:
        data = {
            'full_name': hero.full_name,
            'small_description': hero.small_description,
            'description': hero.description,
            'profile_image': hero.profile_image.url,
            'cv': hero.cv.url
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'No hero found'}, status=404)

def get_about_me(request):
    about_me = AboutMe.objects.first()  # Assuming you have only one about_me entry
    if about_me:
        data = {
            'about_me_para1': about_me.about_me_para1,
            'about_me_para2': about_me.about_me_para2,
            'years_of_experience': about_me.years_of_experience,
            'projects': about_me.projects,
            'happy_clients': about_me.happy_clients,
            'about_me_image': about_me.about_me_image.url,
            
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'No about_me found'}, status=404)



def get_skills(request):
    skills = Skill.objects.all()  # Fetch all skills from the database
    if skills.exists():  # Check if any skills are available
        data = [
            {
                'id': skill.id,  # Add ID if needed for React keys
                'name': skill.name,
                'percentage': skill.percentage,
            } for skill in skills
        ]
        return JsonResponse(data, safe=False)  # Return a list of skills
    return JsonResponse({'error': 'No skills found'}, status=404)


def get_logo(request):
    logos = Logo.objects.all()  # Fetch all logo entries
    if logos.exists():  # Check if any logos are available
        data = [
            {
                'id': logo.id,
                'logo_image': logo.logo_image.url if logo.logo_image else None,  # Convert to URL if exists
            } for logo in logos
        ]
        return JsonResponse(data, safe=False)  # Return a list of logos
    return JsonResponse({'error': 'No logos found'}, status=404)




def get_services(request):
    services = Service.objects.all()  # Fetch all services from the database
    if services.exists():  # Check if any services are available
        data = [
            {
                'id': service.id,  # Use `service.id` for each service
                'numro_service': service.numro_service,
                'service_name': service.service_name,
                'service_description': service.service_description,
            } for service in services
        ]
        return JsonResponse(data, safe=False)  # Return a list of services
    return JsonResponse({'error': 'No services found'}, status=404)



def get_works(request):
    works = MyWork.objects.all()  # Fetch all works from the database
    if works.exists():  # Check if any works are available
        data = [
            {
                'project_imagee': work.project_imagee.url if work.project_imagee else None,  # Get the image URL
                'project_url': work.project_url,
            } for work in works
        ]
        return JsonResponse(data, safe=False)  # Return a list of works
    return JsonResponse({'error': 'No works found'}, status=404)





def get_contact(request):
    contact = Contact.objects.first()  # Assuming you have only one hero entry
    if contact:
        data = {
            'contact_para': contact.contact_para,
            'phone_number': contact.phone_number,
            'localisation': contact.localisation,
            'email': contact.email,
           
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'No contact found'}, status=404)