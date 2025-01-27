from django.shortcuts import render ,get_object_or_404
from contact_module.forms import ContactForm
from django.contrib import messages
from .models import PersonalInformation,PersonalLastestWork
# Create your views here.

def index(request):
    person = PersonalInformation.objects.all()
    return render (request,'home_module/resume_page.html',{
        'person': person
    })

def site_header_component(request):
    return render(request, 'shared/site_header_component.html',{})

def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html',{})


def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد.')
            contact_form = ContactForm()  
    else:
        contact_form = ContactForm()
    
    return render(request, 'home_module/resume_page.html', { 'form': contact_form })


