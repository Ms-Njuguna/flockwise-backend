"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from farm.views import (
    FlockViewSet,
    EggRecordViewSet,
    BirdSaleViewSet,
    ExpenseViewSet,
)

router = DefaultRouter()
router.register("flock", FlockViewSet)
router.register("eggs", EggRecordViewSet)
router.register("bird-sales", BirdSaleViewSet)
router.register("expenses", ExpenseViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]