from unicodedata import name
from django import views
from django.urls import path
#import virtualenv
from . import views

from App.controler import auth
urlpatterns = [
    path('accueill/', views.accueill , name='Accueill'),
    path('register/', auth.register, name='register'),
    path('', auth.loginpage, name='loginpage'),
    path('logout/', auth.logoutpage, name='logoutpage'),
    path('add_etu/', views.add_etu, name='add_etu'),
    path('add_emp/', views.add_emp, name='add_emp'),
    
    #path('classes/', views.classes, name='classes'),
    path('Plus/', views.Plus, name='Plus'),
    path('Ann/', views.Ann,name='Ann'),
    #path('Matiers/', views.Matiers, name='Matiers'),
    path('Clss/', views.Clss, name='Clss'),
    #path('unClass/<id>/', views.unClass, name='unClass'),
    #path('detail/<id>', views.detail, name='detail'),
    #path('Abs/<id>', views.Abs, name='Abs'),
    #path('ListAbs/<id>', views.ListAbs, name='ListAbs'),
    #path('paranh/', auth.loginpage, name='paranh'),
    #path('Notes/<id>', views.Notes, name='Notes'),
    #path('supNot/<id>', views.supNot, name='supNot'),
    #path('supAbs/<id>', views.supAbs, name='supAbs'),
    #path('Paiment/<id>', views.Paiment, name='Paiment'),
    #path('Pay/<id>', views.Pay, name='Pay')
]
