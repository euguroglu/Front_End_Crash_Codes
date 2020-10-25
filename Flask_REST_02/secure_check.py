

from user import User

users = [User(1,'Jose','mypassword'),
         User(2,'Mimi','secret')]

username_table = {u.username: u for u in users}
user_table = {u.id:u for u in users}

def authenticate(username,password):
    #check if user exist
    #if so return users

    user = username_table.get(username,None)
    if user and password == user.password:
        return user

def identity(payload):

    user_id = payload['identity']
    return user_table.get(user_id,None)
