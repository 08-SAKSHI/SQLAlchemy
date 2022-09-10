from re import U
from main import User,Session,engine

local_session = Session(bind = engine)

#this is query to returns all objects
# users = local_session.query(User).all()

# for user in users:
#     print(user.username)

#below query is used for one object

jona = local_session.query(User).filter(User.username=="jona").first()
print(jona)    
    



