from rest_framework import permissions
from authentication.models import User


class Sales_management_Permission(permissions.BasePermission):
    message = "Vous ne faite pas parti de l'équipe de management ou de l'équipe de vente"

    def has_object_permission(self, request, view, obj):
        user = User.objects.get(username=request.user)
        print(user.autorisations)
        if user.autorisations == "MA" or user.autorisations == "SA":
            return obj


class SupportPermission(permissions.BasePermission):
    message = "Vous ne faite pas parti de l'équipe du support"

    def has_object_permission(self, request, view, obj):
        user = User.objects.get(username=request.user)
        if user.autorisations == "SU":
            return obj