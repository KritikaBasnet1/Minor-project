from django.urls import path
from kb import views

urlpatterns = [
    path('', views.index,name='index'),
    path('whytochoose/', views.whytochoose,name='whytochoose'),
    path('login/', views.loginpage,name='login'),
    path('main/', views.mainpage,name='main'),
    path('signup/', views.signuppage,name='signup'),
    path('features/', views.features,name='features'),
    path('client/', views.client,name='client'),
    path('new/', views.new,name='new'),
    path('payment/', views.payment,name='payment'),
    path('esewa/', views.esewa,name='esewa'),
    path('khalti/', views.khalti,name='khalti'),
    path('contact/', views.contact,name='contact'),
    path('bookingForm/', views.bookingForm,name='bookingForm'),
    path('testimonial/', views.testimonial,name='testimonial'),
    path('base/',views.base,name='base'),
    path('users/',views.users,name='users'),
    path('revenue',views.revenue,name='revenue'),
    path('useractivity',views.useractivity,name='useractivity'),
    path('vehiclecatagory1',views.vehiclecatagory,name='vehiclecatagory1'),
  
]