from flask_login import current_user
from website.models import User, Requests



def is_admin (user: User, request: Requests) -> bool:
    """Check if the user can update the state of the given request."""
    if user.role!= 2:
        return False
    
def can_delete_request (user: User, request: Requests, requester_id) -> bool:
    if user.role == 0:
            return False, 'You must be an Admin to delete'
    if user.role == 1 and requester_id !=user.id:
            return False, 'Requesters can only delete their own requests.'
    if (user.role == 1 and requester_id == user.id) or (user.role == 2 ): 
            return True, ''
    return False, 'Unauthorized action.'

def can_create_request (user: User, requested_for_email, ) -> bool:
    if user.role == 0 and requested_for_email != user.email:
            return False, 'Regular Users can only request access for themselves.'
    if user.role in [1,2]:
            return True, ''
    return False, 'Unauthorized action.'

def can_update_request (user: User, requested_for_email, requester_id) -> bool:
      if user.role == 0 and requested_for_email != user.email:
            return False, 'Regular Users can only update their own requests.'
      if user.role == 1 and requester_id !=user.id:
            return False, 'Requesters can only update their own requests.'
      if user.role not in [0,1,2]:
        return False, 'Unauthorized action.'
      else:
        return True, ''  
      
def can_view_request (user: User, request: Requests) -> bool:
    if user.role == 2:
            return True
    if request.requester_id==user.id:
            return True
    
    if request.requested_for_email==user.email:
            return True, ''
    else:
        return False, 'Unauthorized action.'
