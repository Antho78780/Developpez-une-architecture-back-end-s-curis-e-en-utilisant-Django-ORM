from rest_framework import serializers
from .models import Customer, Contract, Event

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["firstname", "lastname", "email", "mobile", "compagny_name", "date_created", "date_updated"]


class ContractSerialier(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ["contract_status", "amount", "customer", "date_created", "date_updated"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["contract", "date_created", "date_updated"]