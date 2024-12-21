from django.urls import path
from .views import *
app_name = 'webpage'

urlpatterns = [path('',home,name='home'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('callback/',callback,name='callback'),
    path('login/',login,name='login'),
    path('frontendDomination/',frontendDomination,name='frontendDomination'),
    path('backendDomination/',backendDomination,name='backendDomination'),
    path('aptitude/',aptitude,name='aptitude'),
    path('DSA/',DSA,name='DSA'),
]
