from schemas.database_model import User

def add_user(user,session):
    u = User(
        name = user.name,
        email = user.email,
        password = user.password,
        role = user.role
    )
    session.add(u)
    session.commit()
    return "user created."

def update_user(email,u,session):
    user = session.query(User).filter_by(email=email).one_or_none()
    if user:
        if u.name:
            user.name = u.name
        session.commit()
        return "user updated."

def delete_user(email,session):
    user = session.query(User).filter_by(email=email).one_or_none()
    if user:
        session.delete(user)
        session.commit()
        return "user deleted."
    
def show_users(session):
    users = session.query(User).all()
    return users

def show_user(email,session):
    user = session.query(User).filter_by(email=email).one_or_none()
    return user

def get_user_by_id(id,session):
    user = session.query(User).filter_by(id=id).one_or_none()
    return user