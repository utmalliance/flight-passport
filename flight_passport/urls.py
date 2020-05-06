"""flight_passport URL Configuration

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
from django.urls import include, path
from vault import views as vault_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
    path("oauth/userinfo/",vault_views.get_user, {}, 'current_user'),
    path("oauth/jwks.json",vault_views.GetJWKS.as_view(), name='get-jwks'),
    path("oauth/", include('oauth2_provider_jwt.urls', namespace='oauth2_provider_jwt')),
    path("accounts/", include('allauth.urls')),
]
