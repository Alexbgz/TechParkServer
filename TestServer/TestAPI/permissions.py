from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    """Allow everyone to list or view, but only the other can modify existing instances"""
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        if obj is None:
            # Either a list or a create, so no author
            can_edit = True
        else:
            can_edit = request.user == obj
        return can_edit
