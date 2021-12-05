
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("serviceaccount.json")
firebase_admin.initialize_app(cred)


db=firestore.client()

docs=db.collection('Graph').document('7ohnu5NiY2936JSa0Foo')
print(docs.get())
#for doc in docs:
#    print(doc.to_dict())