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
    
    path('classes/', views.classes, name='classes'),
    path('GSP/', views.GSP, name='GSP'),
    path('Dep/', views.Dep, name='Dep'),
    path('Plus/', views.Plus, name='Plus'),
    path('Ann/', views.Ann,name='Ann'),
    #path('Matiers/', views.Matiers, name='Matiers'),
    path('Clss/', views.Clss, name='Clss'),
    path('ADD/', views.ADD, name='ADD'),
    path('unClass/<id>/', views.unClass, name='unClass'),
    path('EtuP/<id>/', views.EtuP, name='EtuP'),
    path('supEtu/<id>', views.supEtu, name='supEtu'),
    path('UP/<id>', views.UP, name='UP'),

    path('detail/<id>', views.detail, name='detail'),
    #path('Abs/<id>', views.Abs, name='Abs'),
    #path('ListAbs/<id>', views.ListAbs, name='ListAbs'),
    #path('paranh/', auth.loginpage, name='paranh'),
    #path('Notes/<id>', views.Notes, name='Notes'),
    #path('supNot/<id>', views.supNot, name='supNot'),
    #path('supAbs/<id>', views.supAbs, name='supAbs'),
    path('Paiment/<id>', views.Paiment, name='Paiment'),
    path('Pay/<id>', views.Pay, name='Pay'),
    path('SalaireEmp/<id>', views.SalaireEmp, name='SalaireEmp'),
    path('Credite/<id>', views.Credite, name='Credite'),
    path('Return/<id>', views.Return, name='Return'),
    path('ReturnClasse/<id>', views.ReturnClasse, name='ReturnClasse'),
]
