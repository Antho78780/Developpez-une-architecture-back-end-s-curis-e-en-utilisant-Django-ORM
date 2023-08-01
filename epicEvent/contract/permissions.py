from rest_framework import permissions
from authentication.models import User


class Sales_management_Permission(permissions.BasePermission):
    message = "vous ne disposez pas des privilèges suffisants pour faire cette action"

    def has_object_permission(self, request, view, obj):
        user = User.objects.get(username=request.user)
        print(obj[0])
        if user.autorisations == "MA":
            return obj
        if user.autorisations == "SA" and request.user == obj[0].sales_contact:
            return obj
        


class SupportPermission(permissions.BasePermission):
    message = "Vous ne faite pas parti de l'équipe du support"

    def has_object_permission(self, request, view, obj):
        user = User.objects.get(username=request.user)
        if user.autorisations == "SU":
            if request.method == "GET" or request.method == "PUT":
                return obj