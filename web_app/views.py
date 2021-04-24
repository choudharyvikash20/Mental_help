from django.shortcuts import render,redirect
import pyrebase
from django.contrib import auth

firebaseConfig = {
    "apiKey": "AIzaSyBwvRaCjGS2139_a1F9zjRbcNdhMh3drs8",
    "authDomain": "mental-help-19.firebaseapp.com",
    "projectId": "mental-help-19",
    "storageBucket": "mental-help-19.appspot.com",
    "messagingSenderId": "364528486266",
    "databaseURL": "https://mental-help-19-default-rtdb.firebaseio.com",
    "appId": "1:364528486266:web:40b2cbca111762a59078c3",
    "measurementId": "G-SNRNRSN5XZ"
  };
firebase = pyrebase.initialize_app(firebaseConfig)

authe = firebase.auth()
database = firebase.database()


def testing(request):
    return render(request,'testing.html')

def login(request):
    email=request.POST.get('email')
    pasw=request.POST.get('password')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,'index.html',{"message":message})
    session_id=user['idToken']
    print(user)
    request.session['uid']=str(session_id)
    message ="done";
    return render(request,'dashboard.html',{"email":email,"message":message,'some_flag': True})

def signup(request):
    name = request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('password')
    c_passw=request.POST.get('c-password')
    user=authe.create_user_with_email_and_password(email,passw)
    uid =user['localId']
    data={"name":name,"status":"1"}

    database.child("users").child(uid).child("details").set(data)
    return redirect('homepage')


def homepage(request):
    return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect('homepage')

def dashboard(request):
    return render(request,'dashboard.html')

def mysession(request):
    return render(request,'mysession.html')

def profile(request):
    return render(request,'profile_user.html')
