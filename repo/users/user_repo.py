from schemas.database_model import User,Role

async def add_user(user,session):
    u = User(
        name = user.name,
        email = user.email,
        password = user.password,
        role = user.role
    )
    await session.add(u)
    await session.commit()
    return "user created."

async def update_user(email,u,session):
    user = session.query(User).filter_by(email=email).one_or_none()
    if user:
        if u.name:
            user.name = u.name
        await session.commit()
        return "user updated."

async def delete_user(email,session):
    user = session.query(User).filter_by(email=email).one_or_none()
    if user:
        await session.delete(user)
        await session.commit()
        return "user deleted."
    
async def show_users(username,sort_query,search_by,filter_by,session):
    query = await session.query(User)
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

async def show_user(email,session):
    user = await session.query(User).filter_by(email=email).one_or_none()
    return user

async def get_user_by_id(id,session):
    user = await session.query(User).filter_by(id=id).one_or_none()
    return user
