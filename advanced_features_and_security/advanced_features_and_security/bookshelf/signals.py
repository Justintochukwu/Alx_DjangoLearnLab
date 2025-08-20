from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == "bookshelf":  # change bookshelf to your app name
        # Get all permissions for Book model
        book_model = apps.get_model("bookshelf", "Book")
        permissions = Permission.objects.filter(content_type__app_label="bookshelf", content_type__model="book")

        # Define groups and assign permissions
        group_permissions = {
            "Editors": ["can_edit", "can_create"],
            "Viewers": ["can_view"],
            "Admins": ["can_edit", "can_create", "can_delete", "can_view"],
        }

        for group_name, perm_codes in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for code in perm_codes:
                perm = permissions.filter(codename=code).first()
                if perm:
                    group.permissions.add(perm)
