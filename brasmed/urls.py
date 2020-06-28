from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import *

admin.site.site_header = 'BRASMED'
admin.site.site_title = 'BRASMED'

urlpatterns = \
    [
        path('admin/', admin.site.urls),
        path('', administrador),
        path('login/', login_user),
        path('solicitacoes/', include('solicitacao.urls')),
        path('login/submit', submit_login),
        path('logout/', logout),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                               document_root=settings.STATIC_ROOT)
