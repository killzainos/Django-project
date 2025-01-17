from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import WeAreDeconsult,OurService
from django.shortcuts import render, get_object_or_404
# Create your views here.
class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options = WeAreDeconsult.objects.first()
        services = OurService.objects.all()
        
        context = {
            'options': options,
            'services':services,
        }
        
        return context
    
def servicedetail(request,slug):
    details = get_object_or_404(OurService,slug=slug)
    context = {
        'details' : details,
    }
    return render(request,'home_module/service_detail.html',context)   
    
def site_header_component(request):
    return render(request,'shared/site_header_component.html')

def site_footer_component(request):
    return render(request,'shared/site_footer_component.html')

