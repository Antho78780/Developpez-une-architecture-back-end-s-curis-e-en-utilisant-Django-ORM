from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Contract, Event
from .serializers import CustomerSerializer, ContractSerialier, EventSerializer

class CustomerViewSet(viewsets.ModelViewSet):
   serializer_class = CustomerSerializer


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerialier


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
