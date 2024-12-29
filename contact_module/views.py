from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Email body
        email_body = f"""
        New message from Plant Shop Contact Form
        
        From: {name} ({email})
        Subject: {subject}
        
        Message:
        {message}
        """
        
        try:
            # Send email
            send_mail(
                subject=f'Contact Form: {subject}',
                message=email_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.CONTACT_EMAIL],  # Your email address
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact:contact')
        except Exception as e:
            messages.error(request, 'An error occurred while sending your message. Please try again.')
    
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
