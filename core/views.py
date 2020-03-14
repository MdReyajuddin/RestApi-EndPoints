from django.shortcuts import render
from rest_framework.mixins import (ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin)
from rest_framework.viewsets import GenericViewSet

from .serializers import CompanySerializer
from .models import Company


# Create your views here.
class CompanyViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()



