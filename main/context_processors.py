from .models import *

def is_staff(request):
    # Get user_id from session with a default value of None
    user_id = request.session.get('user_id', None)
    if user_id is not None:
        try:
            # Try to retrieve the UserProfile instance
            user = UserProfile.objects.get(pk=user_id)
            # Check if the user is not a student
            if user.role != 'Student':
                return {'is_staff': True}
        except UserProfile.DoesNotExist:
            pass  # Handle the case where UserProfile with given user_id doesn't exist
    # If user_id doesn't exist in session or if the user is a student, return False
    return {'is_staff': False}