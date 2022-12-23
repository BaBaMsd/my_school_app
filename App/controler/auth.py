
from multiprocessing import context
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from App.models import *

from App.forms import UserForm

def  register(request):
    etu_g = Etudiant.objects.values_list('nom_ag', flat=True)
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if etu_g:
            if form.is_valid():
                username = form.cleaned_data['username']
                
                for i in etu_g:   
                    if i == username:
                        form.save()
                        messages.success(request, 'Vous avez creer un compte parant avec succes')
                        return redirect('/')
                    

    context = {'form': form }
    return render(request, 'user/auth/register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
           # messages.warning(request, '')
            return redirect('accueill/')
        else:
            pop = request.user
            etu = Etudiant.objects.filter(nom_ag=pop)
            context = {
                'etu': etu
            }
            return render(request, 'paranh.html', context)
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                  #  messages.success(request, 'logedd success')
                    return redirect('accueill/')
                else:
                    pop = request.user
                    etu = Etudiant.objects.filter(nom_ag=pop)
                    context = {
                        'etu': etu
                    }
                    messages.success(request, 'logedd success')
                    return render(request, 'paranh.html', context)
            else:
                messages.error(request, 'nom ou mot pass invalid ')
                return redirect('/')
        return render(request, 'user/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
       # messages.success(request, 'Deconnexion ')
    return redirect('/')