from flask import session


def current_user():
    if 'id' in session:
        uid = session['id']
        return User.query.get(uid)
    return None
