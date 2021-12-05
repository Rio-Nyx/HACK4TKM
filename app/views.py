
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import pyrebase
global firebase,db,auth
from . import Adjacency_mat as AM
firebaseConfig = {
  "apiKey": "AIzaSyACoOC6Vg9Yuff-Su_1hX7O-9jwg8qScMQ",
  "authDomain": "test-12f7a.firebaseapp.com",
  "projectId": "test-12f7a",
 "databaseURL": "https://test-12f7a-default-rtdb.firebaseio.com",
  "storageBucket": "test-12f7a.appspot.com",
  "messagingSenderId": "153279384591",
  "appId": "1:153279384591:web:beb62e392740ba308da77a",
}#firebase = pyrebase.initialize_app(firebaseConfig)
#firebase=pyrebase.initialize_app(firebaseConfig)

def index(request):

    return render(request,'index.html')


def login(request):
    return render(request, 'login.html')

def create(request):
    pass


def auth(request):

    try:
        AM.get_short_path(60)
        firebase = pyrebase.initialize_app(firebaseConfig)
        db = firebase.database()
        auth = firebase.auth()
        username=request.POST['fname']
        password = request.POST['pswd']
        auth.sign_in_with_email_and_password(username,password)
        print(auth.current_user['email'])
        context = {'user': auth.current_user['email']}
        return render(request, 'home.html',context)
    except:
        context = {'error': 'E-mail id/ Password is invalid'}
        return render(request, 'login.html',context)

def submit(request):

    firebase = pyrebase.initialize_app(firebaseConfig)
    db=firebase.database()
    auth=firebase.auth()

    username=request.POST['fname']
    name=request.POST['name']
    password=request.POST['pswd']
    #type=request.POST['user_type']
    print(username)
    print(name)
    print(password)

    try:
        auth.create_user_with_email_and_password(username,password)
    except Exception as e:
        print("Enter valid e mail id")
        context = {'error':'Enter valid e-mail id'}
        return render(request, 'index.html',context)
    else:
        print(name)
        print(username)
        print(password)
        print(type)
        print("hi")

        return render(request, 'login.html')