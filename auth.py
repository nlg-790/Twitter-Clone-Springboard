from flask import session


def get_current_user():
    """Get the currently logged-in user."""
    if 'user_id' in session:
        user_id = session['user_id']
        # Retrieve the user from the database using the user_id
        user = user.query.get(user_id)
        return user
    else:
        return None