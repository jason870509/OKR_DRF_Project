from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
	perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
	
	def has_permission(self, request, view):
		# print(request.user.get_all_permissions())
		print("HERE AUTH", request.user.is_staff)
		if not request.user.is_staff:
			return False
		return super().has_permission(request, view)