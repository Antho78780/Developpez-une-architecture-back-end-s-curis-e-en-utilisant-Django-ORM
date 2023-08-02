from rest_framework import permissions
from authentication.models import User


class SalesManagementPermission(permissions.BasePermission):
    message = "vous ne disposez pas des privilèges suffisants pour faire cette action"

    def has_object_permission(self, request, view, obj):
        user = User.objects.get(username=request.user)
        if user.autorisations == "MA":
            return obj
        
        elif user.autorisations == "SA" and request.method == "POST":
            return obj
            
        elif user.autorisations == "SA":
            if request.method == "GET" or request.method == "PUT":
                if request.user == obj[0].sales_contact:
                    return obj
            
    

class SupportsManagementPermission(permissions.BasePermission):
    message = "vous ne disposez pas des privilèges suffisants pour faire cette action"

    def has_object_permission(self, request, view, obj):
        user = User.objects.get(username=request.user)
        if user.autorisations == "MA":
            return obj
        
        elif user.autorisations == "SA" and request.method == "POST":
                return obj
            
        elif user.autorisations == "SU":
            if request.method == "GET" or request.method == "PUT":
                if request.user == obj[0].support_contact:
                    return obj