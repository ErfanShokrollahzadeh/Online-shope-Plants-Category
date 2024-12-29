from django.shortcuts import render

def contact_view(request):
    contact_info = {
        'address': '123 Plant Street, Green City, GC 12345',
        'email': 'info@plantshop.com',
        'phone': '+1 (555) 123-4567',
        'hours': 'Monday - Friday: 9:00 AM - 6:00 PM',
        'social_media': {
            'facebook': 'https://facebook.com/plantshop',
            'instagram': 'https://instagram.com/plantshop',
            'twitter': 'https://twitter.com/plantshop',
            'linkedin': 'https://linkedin.com/company/plantshop'
        }
    }
    return render(request, 'contact_module/contact.html', {'contact_info': contact_info})

# Create your views here.
