from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('home',views.home,name='home'),
    path('booking',views.booking,name='booking'),
    path('doctors',views.doctors,name='doctors'),
    path('payment',views.payment,name='payment'),
    path('feedback',views.feedback,name='feedback'),
    path('signup',views.signup,name='signup'),
    path('login',views.loginn,name='login'),
    path('about',views.about,name='about'),


]
