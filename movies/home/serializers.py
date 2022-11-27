from rest_framework import serializers
from .models import moviesinfo,Contact

class movieapi(serializers.ModelSerializer):
    class Meta:
        model=moviesinfo
        fields='__all__'
        
class con(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'