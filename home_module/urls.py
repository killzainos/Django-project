from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='index_page'),
    path('<slug:slug>',views.servicedetail,name='service-detail')
]