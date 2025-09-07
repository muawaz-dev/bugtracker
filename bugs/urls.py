from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('report/',views.report,name='report'),
    path('success/',views.success,name='success'),
    path('',include('django.contrib.auth.urls')),
    path('sign-up/',views.sign_up,name='sign_up'),
    
]