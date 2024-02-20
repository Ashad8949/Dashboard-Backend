# dashboard_app/viewsets.py
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Insight
from .serializers import InsightSerializer, DistinctSectorSerializer

class InsightViewSet(viewsets.ModelViewSet):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer


class DistinctSectorAPIView(APIView):
    def get(self, request):
        # Aggregate count of each sector
        sector_counts = Insight.objects.values('sector').annotate(count=Count('sector'))

        # Serialize the data
        serializer = DistinctSectorSerializer(sector_counts, many=True)

        return Response(serializer.data)
