"""brasmed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import *

admin.site.site_header = 'BRASMED'
admin.site.site_title = 'BRASMED'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', administrador),
    path('login/', login_user),
    path('solicitacoes/', include('solicitacao.urls')),
    path('login/submit', submit_login),
    path('logout/', logout),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)