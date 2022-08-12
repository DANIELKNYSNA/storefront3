from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render

# this auto sends an email once the end point is hit /playground/hello/
def say_hello(request):
    try:
        send_mail('subject', 'message', 'info@cws.com', ['bob@cws.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
