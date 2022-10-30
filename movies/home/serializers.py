from rest_framework import serializers
from .models import moviesinfo

class movieapi(serializers.ModelSerializer):
    class Meta:
        model=moviesinfo
        fields='__all__'
        