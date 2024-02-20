# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InsightViewSet, DistinctSectorAPIView

router = DefaultRouter()
router.register(r'insights', InsightViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('distinct-sectors/', DistinctSectorAPIView.as_view(), name='distinct-sectors'),
]

