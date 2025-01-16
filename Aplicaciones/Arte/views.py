from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm
from django.shortcuts import get_object_or_404
from datetime import datetime

def home(request):
    return render(request, 'home.html')
def home1(request):
    return render(request, 'home1.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "¡Usuario creado exitosamente!")
            return redirect('home1') 
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
            return render(request, 'Login/registro.html', {'form': form})
    else:
        form = RegistroUsuarioForm()
    return render(request, 'Login/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        print(request.POST)  
        if 'usuario' in request.POST and 'clave' in request.POST:
            username = request.POST['usuario']
            password = request.POST['clave']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home1')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Campos de usuario o contraseña faltantes.')
    return render(request, 'login/login.html')

