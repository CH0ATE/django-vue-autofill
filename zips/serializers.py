from rest_framework import serializers
from .models import Zip



class ZipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zip
        fields = '__all__'
