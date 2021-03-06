"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.generic import RedirectView
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


urlpatterns = [
    path('', RedirectView.as_view(url='/admin/', permanent=False)),

    path('admin/', admin.site.urls),
    path('{{cookiecutter.project_name}}/', include('{{cookiecutter.project_name}}.urls')),

    path('api/v1/', include('{{cookiecutter.project_name}}.urls_api')),
    path('api/auth/', include('rest_framework.urls')),
    path('api/docs/', include_docs_urls(title='{{cookiecutter.project_name}} API', public=False)),
    path('api/auth-jwt/', obtain_jwt_token),  # POST email=email&password=password
    path('api/auth-jwt-verify/', verify_jwt_token),
    path('api/auth-jwt-refresh/', refresh_jwt_token),

]
