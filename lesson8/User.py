class User ():
    def __init__ (self, name ,email , password):
        self._name = name
        self._email = email
        self._password = password

    def setName (self,name):
        self._name = name

    def setEmail (self,email):
        self._email = email

    def setPassword (self,password):
        self._password = password

    def getName(self):
        return self._name

    def getEmail(self):
        return self._email

    def getPassword(self):
        return self._password

Artem = User("Artem","shvartemm@gmail.com",'qweqweqwe')
print(Artem.getName())
Artem.setName("King")
print(f"I changed Artem`s class name to {Artem.getName()}")
print(Artem.getEmail())
print(Artem.getPassword())


