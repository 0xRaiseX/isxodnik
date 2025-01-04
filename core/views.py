from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model 
# Create your views here.
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomPasswordChangeForm
from .models import ServerConfig, GeoBlock
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request, 'login.html', {'error': 'Неверные данные'})
        
    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def dashboard_finance(request):
    return render(request, 'dashboard_finance.html')

@login_required
def dashboard_settings(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Пароль успешно изменён.')
            return redirect('dashboard_settings')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = CustomPasswordChangeForm(user=request.user)

    configs = ServerConfig.objects.all()

    # Здесь форма добавляется в контекст
    return render(request, 'dashboard_settings.html', {'form': form})

@login_required
def dashboard_help(request):
    return render(request, 'dashboard_help.html')

@login_required
def dashboard_updatedata(request):
    return render(request, 'dashboard_updatedata.html')

def send_email():
    send_mail(
        subject='Тема письма',  # Тема письма
        message='Текст письма',  # Сообщение
        from_email='ваш_почтовый_адрес@ваш_домен.ru',  # Адрес отправителя
        recipient_list=['получатель@example.com'],  # Список получателей
        fail_silently=False,  # Поднимет исключение при ошибке
    )

@login_required
def dashboard_newserver(request):
    configs = ServerConfig.objects.all()
    geo_blocks = GeoBlock.objects.all()

    return render(request, 'dashboard_newserver.html', {'configs': configs, 'geo_blocks': geo_blocks})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Пароли не совпадают'})
        
        if '@' not in username:
            return render(request, 'register.html', {'error': 'Ошибка в логине'})
        
        if get_user_model().objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Пользователь уже существует!'})
        
        user = get_user_model().objects.create_user(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect('/dashboard')
    
    return render(request, 'register.html')