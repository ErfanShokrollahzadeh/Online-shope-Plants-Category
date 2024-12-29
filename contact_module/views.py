from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings
import logging
import ssl
import certifi

logger = logging.getLogger(__name__)

def contact_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            email_body = f"""
New Contact Form Submission

From: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""
            # Configure SSL context
            ssl_context = ssl.create_default_context(cafile=certifi.where())
            
            if subject and message and email:
                send_mail(
                    subject=f'Plant Shop Contact: {subject}',
                    message=email_body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you! Your message has been sent successfully.')
                return redirect('contact:contact')
            else:
                messages.error(request, 'Please fill in all required fields.')
                
        except Exception as e:
            logger.error(f'Error sending email: {str(e)}')
            messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
            
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
