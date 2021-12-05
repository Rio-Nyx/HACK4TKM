
from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse
import pyrebase
from django.views.decorators.csrf import csrf_exempt

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

    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    auth = firebase.auth()
    username=request.POST['fname']
    password = request.POST['pswd']
    auth.sign_in_with_email_and_password(username,password)
    print(auth.current_user['email'])
    context = {'user': auth.current_user['email']}
    return render(request, 'home.html',context)
    #except:
    #    context = {'error': 'E-mail id/ Password is invalid'}
    #    return render(request, 'login.html',context)

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

@csrf_exempt
def compute(request):
    queing_no = 5
    chargingtime = 6


    val_x = request.GET['x']
    val_y = request.GET['y']
    val_x=int(val_x)
    val_y = int(val_y)
    val_fuel = request.GET['fuel']
    print(val_fuel)
    print(val_y)
    print(val_x)

    AM.get_short_path(val_fuel,val_x,val_y)
    l = AM.get_shortest_palces()
    place = ''
    min = 10000
    for i in range(1, len(l)):
        cost = queing_no * chargingtime + l[i][1]
        if (cost < min):
            place = l[i][0]
            min = cost
    print(min)
    print(place)

    response__data = {'place':place,'min':min}
    return JsonResponse(response__data)


def dist(request):
    queing_no = 5
    chargingtime = 6
    fuel = request.POST['fuel']
    x = request.POST['x']
    y = request.POST['y']
    fuel=int(fuel)
    x = int(x)
    y = int(y)
    AM.get_short_path(fuel, x, y)
    l = AM.get_shortest_palces()
    place = ''
    min = 10000
    for i in range(1, len(l)):
        cost = queing_no * chargingtime + l[i][1]
        if (cost < min):
            place = l[i][0]
            min = cost
    print(min)
    print(place)
    context={'place':place,'min':min}
    return render(request, 'result.html',context)

def optimal(request):
    return render(request, 'optimalstations.html')

from . import optimal as OP

def opt(request):
    graph_link=request.POST['graph']
    location_link = request.POST['location']
    print(graph_link)
    print(location_link)
    charging_stations=OP.compute(graph_link,location_link)
    context={'charging_stations':charging_stations}
    return render(request, 'optresult.html',context)
