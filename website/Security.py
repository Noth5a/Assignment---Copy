from flask_login import current_user
from website.models import User, Requests



def is_admin(user: User) -> bool:
    """Check if the user is an admin."""
    return user.role == 2

def can_delete_user(user: User, target_user: User, admin_count: int) -> tuple[bool, str]:
    """Check if the user can delete the target user."""
    if not is_admin(user):
        return False, 'You must be an Admin to delete users'
    elif target_user is None:
        return False, 'Error, User doesnt exist'
    elif target_user.role == 2 and admin_count <= 1:
        return False, 'Cannot delete the last Admin user.'
    elif user.id == target_user.id:
        return False, 'You cannot delete your own account.'
    elif (is_admin(target_user)==False or admin_count > 1) and user.id != target_user.id:
        return True, ''
    else:
        return False, 'Error'

def can_modify_user(user: User, target_user: User, admin_count: int) -> tuple[bool, str]:
    """Check if the user can modify the target user."""
    if not is_admin(user):
        return False, 'You must be an Admin to modify users'
    elif target_user is None:
        return False, 'Error, User doesnt exist'
    elif user.id == target_user.id:
        return False, 'You cannot modify your own account.'
    elif target_user.role == 2 and admin_count <= 1:
        return False, 'Cannot demote the last Admin user.'
    elif (is_admin(target_user)==False or admin_count > 1) and user.id != target_user.id:
        return True, ''
    else:
        return False, 'Error'