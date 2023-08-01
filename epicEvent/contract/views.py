from rest_framework import viewsets
from .models import Customer, Contract, Event
from .serializers import CustomerSerializer, ContractSerialier, EventSerializer
from django.db.models import Q
from contract.permissions import Sales_management_Permission, SupportPermission
from rest_framework.response import Response


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [Sales_management_Permission]
    
    def get_queryset(self):
       if self.request.query_params:
           lastname = self.request.query_params.get("lastname")
           email = self.request.query_params.get("email")
           queryset = Customer.objects.filter(
               Q(lastname=lastname) |
               Q(email=email),
               sales_contact=self.request.user
            )
           return queryset

    
    def perform_create(self, serializer):
        self.check_object_permissions(self.request, serializer)
        serializer.save(sales_contact=self.request.user)

    def update(self, request, *args, **kwargs):
        customer = Customer.objects.filter(id=self.kwargs["pk"])
        self.check_object_permissions(self.request, customer)
        customer.update(
            firstname=self.request.POST["firstname"],
            lastname=self.request.POST["lastname"],
            email=self.request.POST["email"],
            mobile=self.request.POST["mobile"],
            compagny_name=self.request.POST["compagny_name"],
        )
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerialier
    permission_classes = [Sales_management_Permission]

    def get_queryset(self):
        if self.request.query_params:
            lastname = self.request.query_params.get('lastname')
            email = self.request.query_params.get('email')
            amount = self.request.query_params.get('amount')
            date_created = self.request.query_params.get('date_created')
        
            contract = Contract.objects.filter(
                (
                    Q(customer__lastname__iexact=lastname) | 
                    Q(customer__email__iexact=email) | 
                    Q(amount=amount) | 
                    Q(date_created=date_created)
                ),
                sales_contact=self.request.user
            )
            return contract
    
        queryset = Contract.objects.filter(sales_contact=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        self.check_object_permissions(self.request, serializer)
        serializer.save(sales_contact=self.request.user)
    
    def update(self, request, *args, **kwargs):
        contract = Contract.objects.filter(id=self.kwargs["pk"])
        self.check_object_permissions(self.request, contract)
        contract.update(
            amount=self.request.POST["amount"],
            customer=self.request.POST["customer"]
        )
        serializer = ContractSerialier(contract, many=True)
        return Response(serializer.data)
        
        
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [SupportPermission]

    def get_queryset(self):
        if self.request.query_params:
            lastname = self.request.query_params.get('lastname')
            email = self.request.query_params.get('email')
            date_created = self.request.query_params.get('date_created')
            
            event = Event.objects.filter((
                Q(event_status__customer__lastname__iexact=lastname)|
                Q(event_status__customer__email__iexact=email)|
                Q(date_created=date_created))
                ,support_contact=self.request.user
            )
            return event
        queryset = Event.objects.filter(support_contact=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        self.check_object_permissions(self.request, serializer)
        serializer.save(support_contact=self.request.user)
    
    def update(self, request, *args, **kwargs):
        event = Event.objects.filter(id=self.kwargs["pk"])
        self.check_object_permissions(self.request, event)
        event.update(
            notes=self.request.POST["notes"],
            attendees=self.request.POST["attendees"],
            customer=self.request.POST["customer"],
            support_contact=self.request.POST["support_contact"],
            event_status=self.request.POST["event_status"]
        )
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)