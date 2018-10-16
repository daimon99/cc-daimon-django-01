# coding: utf-8

from django.contrib import admin
from django.urls import path, include
import {{cookiecutter.project_name}}.api
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
# router.register('<api>', daydayup.api.<api>)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
