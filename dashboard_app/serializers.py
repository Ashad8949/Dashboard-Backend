# dashboard_app/serializers.py
from rest_framework import serializers
from .models import Insight

class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = '__all__'



class DistinctSectorSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = Insight
        fields = ['sector', 'count']
