import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyACoOC6Vg9Yuff-Su_1hX7O-9jwg8qScMQ",
  "authDomain": "test-12f7a.firebaseapp.com",
  "projectId": "test-12f7a",
 "databaseURL": "https://test-12f7a-default-rtdb.firebaseio.com",
  "storageBucket": "test-12f7a.appspot.com",
  "messagingSenderId": "153279384591",
  "appId": "1:153279384591:web:beb62e392740ba308da77a",
}

firebase = pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
auth=firebase.auth()
username="RAHUL"
password="123456"
auth.create_user_with_email_and_password(username,password)
