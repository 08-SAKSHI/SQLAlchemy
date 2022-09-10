import email

from requests import Session
from main import User,Session,engine 

local_session = Session(bind=engine)

users = [
    {
        "username":"jerry",
        "email": "jerry@company.com"
    },
    {
        "username":"tom",
        "email": "tom@company.com"
    },
    {
        "username":"doremon",
        "email": "doremon@company.com"
    },
    {
        "username":"shinchan",
        "email": "shinchan@company.com"
    },
    {
        "username":"hatori",
        "email": "hatori@company.com"
    },

    {
        "username":"bean",
        "email": "bean@company.com"
    },
    {
        "username":"oggy",
        "email": "oggy@company.com"
    },
]

# new_user= User(username = "jona",email = "jona@company.com")

# local_session.add(new_user)

# local_session.commit()

for u in users:
    new_user = User(username = u["username"],email=u["email"])
    
    local_session.add(new_user)
    local_session.commit()
    
    print(f"Added {u['username']}")
    