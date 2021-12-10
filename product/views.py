from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BaseAuthentication
from rest_framework import filters
# from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class SushiViewSet(viewsets.ModelViewSet):
    queryset = Sushi.objects.all()
    serializer_class = SushiSerializer
    filterset_field = ['name', 'content']
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name', 'price']
    ordering = ['name']
    search_fields = ['name']
    # pagination_class = PageNumberPagination

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class SushiNumberPaginations(PageNumberPagination):
#     page_size = 3

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filterset_field = ['name', 'number']
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name', 'number']
    ordering = ['name']
    search_fields = ['name']

class CardItemViewSet(viewsets.ModelViewSet):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer        
    permission_classes = [IsAuthenticated]
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]