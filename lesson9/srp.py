class User:
    def __init__(self):
        self.username = 'Ortem'
        self.password = 'wordForPass'

class UserManager:

    @staticmethod
    def update(user,username,password):
        user.username = username
        user.password = password
        print(f'Updated Username: {user.username}, and Password: {user.password}')

    @staticmethod
    def remove(user):
        del user.username
        del user.password
        print(f'User has been removed')

    @staticmethod
    def createUser(user):
        user.username = input('Enter username: ')
        user.password = input('Enter password: ')
        print(f'Username: {user.username}, Password: {user.password}')

A = User()
print(f"{A.username}, {A.password}")
UserManager.update(A,A.username,A.password)
UserManager.remove(A)
UserManager.createUser(A)



