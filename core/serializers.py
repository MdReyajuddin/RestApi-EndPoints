from rest_framework import serializers

from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'description', 'website', 'street_line1', 'street_line2', 'city', 'state', 'zip')