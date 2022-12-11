"""bazy_danych URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.uzytkownicy.views import UserRegisterView
from django.contrib.auth import views as auth_views
from apps.produkty.views import AllProductsView
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('uzytkownik/', include('apps.uzytkownicy.urls')),
    path('produkty/', include('apps.produkty.urls')),
    path('zamowienia/', include('apps.zamowienia.urls')),
    path('admin/', admin.site.urls),
    path('', AllProductsView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register-user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
