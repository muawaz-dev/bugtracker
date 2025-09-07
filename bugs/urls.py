from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('report/',views.report,name='report'),
    path('success/',views.success,name='success'),
]