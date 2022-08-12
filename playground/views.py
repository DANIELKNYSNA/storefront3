from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render

# this auto sends an email once the end point is hit /playground/hello/
def say_hello(request):
    try:
        message = EmailMessage('message', 'subject', 'info@cws.com', ['bob@cws.com'])
        message.attach_file('playground/static/images/20210526_152956(0).jpg')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
