"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from user.viewsets import UserViewSet
from auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from finalapp.views import *
router = routers.DefaultRouter()

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router.register('user', UserViewSet, basename='user')
router.register('auth/register', RegisterViewSet, basename='auth-register')
router.register('auth/login', LoginViewSet, basename='auth-login')
router.register('auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register('food', FoodModelViewSet)
router.register('diet', DietModelViewSet)
router.register('breakfast', BreakfastModelViewSet)
router.register('diner', DinerModelViewSet)
router.register('lunch', LunchModelViewSet)
router.register('snacks', SnacksModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    *router.urls,
    # path("", include(router.urls)),
    # OpenAPI 3 documentation with Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
]
