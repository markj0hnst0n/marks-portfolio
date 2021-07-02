from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages

from django.conf import settings

# Create your views here.
def index(request):
    """ A View to return the homepage"""
    
    return render(request, 'home/index.html')

def about(request):
    """ Shows about page"""
    return render(request, 'home/about.html')

def contact(request):
    """ Shows and allows user to sent contact form """

    email = ""
    if request.method == 'POST':
        user_email = request.POST.get("email")
        user_name = request.POST.get("name")
        query = request.POST.get("query")

        owner_subject = render_to_string(
            'home/contact_emails/contact_email_subject.txt')
        owner_body = render_to_string(
            'home/contact_emails/owner_contact_body.txt',
            {'user_name': user_name, 'query': query})

        user_subject = render_to_string(
            'home/contact_emails/contact_email_subject.txt')
        user_body = render_to_string(
            'home/contact_emails/user_contact_email_body.txt')

        send_mail(
            owner_subject,
            owner_body,
            user_email,
            [settings.DEFAULT_FROM_EMAIL]
        )

        send_mail(
            user_subject,
            user_body,
            settings.DEFAULT_FROM_EMAIL,
            [user_email]
        )
        messages.info(request, "Contact form sent")

    context = {
        'email': email,
    }

    return render(request, 'home/contact.html', context)