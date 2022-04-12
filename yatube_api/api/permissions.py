from rest_framework import permissions, status


class IsAuthorOrReadOnly(permissions.BasePermission):

    message = "Вы не можете изменить чужой объект!"
    code = status.HTTP_403_FORBIDDEN

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True

        if (request.user != obj.author
           and request.method in permissions.SAFE_METHODS):
            return True
        return False
