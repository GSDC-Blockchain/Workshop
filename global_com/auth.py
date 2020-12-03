from global_com.firebase_api import database

class User:
    def __init__(self, name = "", email="", password = ""):
        self.name = name
        self.email = email
        self.password = password

    # Create User object from dictionary
    @staticmethod
    def from_dict(source):
        return User(source['name'], source['email'], source['password'])

    # Login
    @staticmethod
    def login(email, password):
        allUsers = database.getAll('users')
        for doc in allUsers:
            if doc.to_dict()['email'] == email and doc.to_dict()['password'] == password:
                return User(doc.to_dict()['name'],email,password)
        return None

    # Registers a new user and returns it
    @staticmethod
    def register(name, email, password):
        # Note: Use of CollectionRef stream() is preferred to get()
        allUsers = database.getAll('users')
        for doc in allUsers:
            if doc.to_dict()['email'] == email:
                return None

        database.addUser(name, email, password)

        return User(name, email, password)



