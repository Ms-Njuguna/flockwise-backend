from django.urls import path, include
from rest_framework.routers import DefaultRouter

from farm.modules.flock.views import FlockViewSet
from farm.modules.income.views import EggRecordViewSet, BirdSaleViewSet
from farm.modules.expenses.views import ExpenseViewSet
from farm.modules.ai.views import ai_assistant

router = DefaultRouter()
router.register("flock", FlockViewSet)
router.register("eggs", EggRecordViewSet)
router.register("bird-sales", BirdSaleViewSet)
router.register("expenses", ExpenseViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/ai/", ai_assistant),
]