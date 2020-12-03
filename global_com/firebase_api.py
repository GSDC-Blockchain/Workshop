import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from .message import _Message
from .settings import SETTINGS
from datetime import datetime


# Database class deals with firestore
class _Database:
    db = object()
    users = object()
    def __init__(self):
        pass

    @classmethod
    def setup(self,path):
        # Use a service account
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred)

        setattr(self, 'db', firestore.client())
        setattr(self, 'users', self.db.collection(SETTINGS['USER_TABLE']))

    # Get all documents from a collection
    def getAll(self, collectionName):
        # Note: Use of CollectionRef stream() is prefered to get()
        return self.db.collection(collectionName).stream()

    def addUser(self, name, email, password):
        self.users.add({
            'name' : name,
            'email' : email,
            'password' : password
        })

        self.db.collection('step').document(email).set({'step': '0'})

    def addMessageChannel(self, user):
        # Protect !
        self.db.collection('message-channels').document(user.email).collection('messages').add({'type' : 'empty'})

    def addMessage(self, channelId, sender, type, content):
        now = datetime.now().time()  # time object
        self.db.collection('message-channels').document(channelId).collection('messages').add({'sender' : sender, 'type': type, 'content': content, 'created': firestore.SERVER_TIMESTAMP})

    def getCollectionByPath(self, path):
        path_arr = path.split('/')
        if len(path_arr) % 2 == 0:
            return None
        curr = self.db
        try:
            for i in range(0, len(path_arr) - 1, 2):

                curr = curr.collection(path_arr[i])
                curr = curr.document(path_arr[i + 1])
            curr = curr.collection(path_arr[len(path_arr)-1])
        except:
            return None
        return curr
    # Ordered | Get and delete
    def getOneDocument(self, path):
        collection = self.getCollectionByPath(path)
        if collection == None:
            return None
        doc = collection.order_by('created').limit(1).get()

        if doc!=None and len(doc) > 0 :
            doc = doc[0]
        else:
            return _Message("","","","")
        collection.document(doc.id).delete()

        return doc

    def deleteAllDocuments(self, path):
        collection = self.getCollectionByPath(path)
        if collection == None:
            return None
        try:
            docs = collection.get()

            for doc in docs:
                collection.document(doc.id).delete()
        except:
            pass
    def getDocuments(self, path, n):
        collection = self.getCollectionByPath(path)
        if collection == None:
            return None
        docs = collection.order_by('created').limit(n).get()

        for doc in docs:
            collection.document(doc.id).delete()

        return docs

    def getStep(self, id):
        return self.db.collection('step').document(id).get().to_dict()['step']

    def incStep(self, id):
        step_doc =  self.db.collection('step').document(id)
        step_doc.set({'step': int(step_doc.get().to_dict()['step'])+1})

    def resetStep(self, id):
        step_doc =  self.db.collection('step').document(id)
        step_doc.set({'step': 0})

database = _Database()

"""
database.setup("C:\\Users\\Filip\\PycharmProjects\\GlobalCommunication\\setup.json")
"""

