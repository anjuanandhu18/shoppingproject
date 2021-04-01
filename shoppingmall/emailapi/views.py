from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from emailapi.forms import SubscribeForm
from django.core.mail import send_mail


''''def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Code Band'
            message = 'Sending Email through Gmail'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('subscribe')
    return render(request, 'emailapi/home2.html', {'form': form})
def send_email(request):
    subject='welcome to GFG world'
    message="hello welcome"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[request.GET['email'],]
    send_mail(subject,message,email_from,recipient_list)
    return redirect('emailapi:email')
def test():
    pass'''''