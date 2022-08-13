from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers

def say_hello(request):
    notify_customers.delay('Hello')    
    return render(request, 'hello.html', {'name': 'Daniel'})
