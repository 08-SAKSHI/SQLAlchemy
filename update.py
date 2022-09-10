from main import Session,engine,User

local_session = Session(bind=engine)

user_to_update = local_session.query(User).filter(User.username=="doremi").first()

user_to_update.username = "doremon"
user_to_update.email = "doremon@company.com"

local_session.commit()

