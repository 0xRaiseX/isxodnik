from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), # Главная страница
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/finance', views.dashboard_finance, name='dashboard_finance'),
    path('dashboard/settings', views.dashboard_settings, name='dashboard_settings'),
    path('dashboard/help', views.dashboard_help, name='dashboard_help'),
    path('dashboard/newserver', views.dashboard_newserver, name='dashboard_newserver'),
    path('dashboard/updatedata', views.dashboard_updatedata, name='dashboard_updatedata'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)