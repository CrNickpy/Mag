from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.post_contact, name='contact'),
    path('get_otz/',views.get_otz,name='otzyv' ),
    path('otzyvy/',Otzyvy.as_view(),name='otzyvy' ),
    path('postcont/', views.p_phone, name='postcont'),
    path('avt/', AvtHome.as_view(), name='avt' ),
    path('exc/', ExcHome.as_view(), name='exc' ),
    path('ssv/', SsvHome.as_view(), name='ssv' ),
    path('pr/', PrHome.as_view(), name='pr' ),
    path('numer/<int:numer_id>/',ShowNumer.as_view(),name='numer'),



] 
