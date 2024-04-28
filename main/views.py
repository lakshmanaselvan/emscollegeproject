from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from .forms import ApplyForm
from django.core.mail import send_mail
from main.models import UserProfile
from .forms import RegistrationForm
from django.conf import settings
from .forms import EventForm
from .models import Event
from datetime import date

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.save()
            token = user_profile.token
            domain_name = get_current_site(request).domain
            verified_link = f'http://{domain_name}/verified/{token}'
            send_mail (
                'Email Verification',
                f'Please click this following link to verify your email: {verified_link}',
                settings.EMAIL_HOST_USER,
                [user_profile.email],
                fail_silently =False
            )
            return render(request, 'registrationSuccess.html', {})
    else:
        form = RegistrationForm()
    return render(request, 'registrationForm.html', {'form': form})

def verified(request, token):
    try:
        user = get_object_or_404(UserProfile, token = token)
        if not user.is_verified:
            user.is_verified = True
            user.save()
            return render(request, 'success.html', {})
    except Exception as e:
        msg = str(e)
        return render(request, 'registrationForm.html', {'msg':msg})

def login(request):
    message = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user_profile = UserProfile.objects.get(email=email)
            if check_password(password, user_profile.password):
                if user_profile.is_verified:
                    print('Hai')
                    request.session['user_id'] = user_profile.id 
                    if user_profile.role.role == 'Student':
                        return redirect(view_event)
                    else:
                        return redirect(profile)
                else:
                    message = 'Your Email Is Not Verified'
                    return render(request, 'login.html', {'message': message})
            else:
                message = 'Invalid Email or Password'
                return render(request, 'login.html', {'message':message})
        except ObjectDoesNotExist:
            message = 'Does Not User Found'
    return render(request, 'login.html', {'message':message})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
           user_id = request.session.get('user_id')
           if user_id:
                # Retrieve the user object using the user ID
                user = UserProfile.objects.get(pk=user_id)
                # Associate the user with the event being created
                event = form.save(commit=False)
                event.organizer = user
                event.save()
                subject = 'Event Approval Request'
                html_message = render_to_string('approval_email.html', {'event': event})
                plain_message = strip_tags(html_message)
                from_email =  user.email 
                to_email = settings.EMAIL_HOST_USER 
                send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
                return render(request, 'eventSuccess.html', {})
           else:
                return render(request, 'create_event.html', {'form':form})
    else:
        form = EventForm()
        return render(request, 'create_event.html', {'form':form})

def apply_event(request):
    form = ApplyForm()
    return render(request, 'applyEvent.html', {'form':form})

def view_event(request):
    today = date.today()
    event_list = Event.objects.all()
    return render(request, "event_list.html", {'event_list':event_list, 'today': today})

def profile(request):
    user_id = request.session.get('user_id')
    event = Event.objects.filter(organizer=user_id)
    user = UserProfile.objects.get(pk=user_id)
    print(user)
    return render(request, 'profile.html', {'event': event,'current_user':user})

def logout(request):
    request.session.clear()
    return redirect(login)

def approve_event(request, id):
    event = get_object_or_404(Event, pk=id)
    event.approval = True
    event.save()
    return redirect('event_details', id=id)

def event_details(request, id):
     event = get_object_or_404(Event, pk=id)
     return render(request, 'event_details.html', {'event': event})

def delete(request, id):
    event = get_object_or_404(Event, pk=id)
    event.delete()
    return redirect(profile)

def EditEvent(request, id):
    event = get_object_or_404(Event, pk=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_details', id)
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form, 'event': event})
