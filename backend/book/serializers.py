from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
        )
        model = Review
