from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        permission_string = self.__get_permission_string(
            method=request.method,
            view=view,
        )
        if not permission_string:
            return False

        return request.user.has_perm(permission_string)

    def __get_permission_string(self, method, view):
        try:
            app_label = view.queryset.model._meta.app_label
            model_name = view.queryset.model._meta.model_name
            action = self.__get_action_sufix(method)
            return f'{app_label}.{action}_{model_name}'

        except AttributeError:
            return None

    def __get_action_sufix(self, method):
        method_actions = {
            "GET": "view",
            "OPTIONS": "view",
            "HEAD": "view",
            "POST": "add",
            "PUT": "change",
            "PATCH": "change",
            "DELETE": "delete",
        }
        return method_actions.get(method, "")
