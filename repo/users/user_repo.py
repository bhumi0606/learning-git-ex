from schemas.database_model import User,Role

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
    
def show_users(username,sort_query,search_by,filter_by,session):
    query = session.query(User)
    if sort_query:
        if sort_query == "username":
            query = query.order_by(User.name)
        if sort_query == "-username":
            query = query.order_by(User.name.desc())

        if sort_query == "email":
            query = query.order_by(User.email)
        if sort_query == "-email":
            query = query.order_by(User.email.desc())
        
        if sort_query == "created_at":
            query = query.order_by(User.created_at)
        if sort_query == "-created_at":
            query = query.order_by(User.created_at.desc())
    
    if filter_by:
        if filter_by == "user":
            query = query.filter(User.role == Role.USER)
        if filter_by == "admin":
            query = query.filter(User.role == Role.ADMIN)

    if username:
        query = query.filter(User.name.ilike(f'%{username}%'))

    if search_by:
        query = query.filter_by(email=search_by)

    users = query.all()
    return users

def show_user(email,session):
    user = session.query(User).filter_by(email=email).one_or_none()
    return user

def get_user_by_id(id,session):
    user = session.query(User).filter_by(id=id).one_or_none()
    return user

def get_users(session):
    users = session.query(User).filter_by(role=Role.USER).all()
    return users

def get_admins(session):
    admins = session.query(User).filter_by(role=Role.ADMIN).all()
    return admins