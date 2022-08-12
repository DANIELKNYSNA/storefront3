from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage

# this auto sends an email once the end point is hit /playground/hello/
def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html', 
            context={'name': 'Daniel'}
        )
        message.send(['bob@cws.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Daniel'})
