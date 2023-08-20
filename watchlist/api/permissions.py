from rest_framework import permissions




class AdminOrReadOnly(permissions.IsAdminUser):
    

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
    # def has_permission(self, request, view):
    #     return super().has_permission(request, view)


class AuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user == obj.author)
        

    
        