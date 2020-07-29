"""SnowManAPI URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = "core"

schema_view = get_schema_view(
    openapi.Info(
        title="Snowman Backend Challeng API",
        default_version='v1',
        description="Ferramenta para teste de endpoints da API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jmdinfo123@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('admin/', admin.site.urls),
    path('api/category', include('apps.category.urls')),
    path('api/tourist-spot/', include('apps.tourist_spot.urls')),
    path('api/user-favorites/', include('apps.favorite.urls')),
    path('api/auth/', include('apps.auth_user.urls')),

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()