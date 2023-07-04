from rest_framework import viewsets
from .models import Customer, Contract, Event
from .serializers import CustomerSerializer, ContractSerialier, EventSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from authentication.models import User
from contract.permissions import AccesPermissionCustomer



class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['lastname', 'email']
    permission_classes = [AccesPermissionCustomer]
    
    def get_queryset(self):
        queryset = Customer.objects.all()
        return queryset
    def perform_create(self, serializer):
        self.check_object_permissions(self.request, serializer)
        user = User.objects.get(username=self.request.user)
        serializer.save(sales_contact=user)
   
    

class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerialier

    def get_queryset(self):
        if self.request.query_params:
            lastname = self.request.query_params.get('lastname')
            email = self.request.query_params.get('email')
            amount = self.request.query_params.get('amount')
            date_created = self.request.query_params.get('date_created')
        
            contract = Contract.objects.filter(Q(customer__lastname__iexact=lastname) | Q(customer__email__iexact=email) | Q(amount=amount) | Q(date_created=date_created))
            return contract
    
        queryset = Contract.objects.all()
        return queryset
        

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        if self.request.query_params:
            lastname = self.request.query_params.get('lastname')
            email = self.request.query_params.get('email')
            date_created = self.request.query_params.get('date_created')
            
            event = Event.objects.filter(Q(contract__customer__lastname__iexact=lastname) | Q(contract__customer__email__iexact=email) | Q(date_created=date_created))
            return event
        
        queryset = Event.objects.all()
        return queryset

        
      