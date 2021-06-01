from django_graphene_permissions.permissions import BasePermission

class IsStaff(BasePermission):
    def has_permission(context):
        return context.user and context.user.is_authenticated and context.user.is_staff