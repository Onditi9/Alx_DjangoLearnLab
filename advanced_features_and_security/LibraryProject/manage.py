from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

# Get content type for Book model
content_type = ContentType.objects.get_for_model(Book)

# Fetch permissions
view_perm = Permission.objects.get(codename="can_view", content_type=content_type)
create_perm = Permission.objects.get(codename="can_create", content_type=content_type)
edit_perm = Permission.objects.get(codename="can_edit", content_type=content_type)
delete_perm = Permission.objects.get(codename="can_delete", content_type=content_type)

# Create groups
viewers, _ = Group.objects.get_or_create(name="Viewers")
editors, _ = Group.objects.get_or_create(name="Editors")
admins, _ = Group.objects.get_or_create(name="Admins")

# Assign permissions
viewers.permissions.add(view_perm)

editors.permissions.add(view_perm, create_perm, edit_perm)

admins.permissions.add(view_perm, create_perm, edit_perm, delete_perm)


