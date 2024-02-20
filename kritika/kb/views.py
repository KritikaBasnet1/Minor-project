from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from . models import userinfo
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login

def index(request):
    return render (request,'index.html')

def features(request):
    return render(request,'features.html')

def whytochoose(request):
    return render(request,'whytochoose.html')

def client(request):
    return render(request,'client.html')

def new(request):
    return render(request,'new.html')

def payment(request):
    return render(request,'payment.html')

def esewa(request):
    return render(request,'esewa.html')

def khalti(request):
    return render(request,'khalti.html')

def contact(request):
    return render(request,'contact.html')

def bookingForm(request):
    return render(request,'bookingForm.html')

def testimonial(request):
    return render(request,'testimonial.html')


# def logout(request):
#     messages.success(request,"Logout successfully")
#     return redirect('/')
def base(request):
    return render(request,'base.html')

def users(request):
    userlist= userinfo.objects.all()
    return render(request,'users.html',{'userlist':userlist})

def signup(request):
    try:
        if request.method == "POST":
            obj = userinfo()
            obj.name = request.POST.get('name','')
            print(obj.name)
            obj.email = request.POST.get('email','')
            print(obj.email)
            obj.phone = request.POST.get('phone','')
            print(obj.phone)
            obj.username = request.POST.get('username','')
            print(obj.username)
            obj.password = request.POST.get('pass','')
            print(obj.password)
            
            usrlst = userinfo.objects.values_list('username',flat=True)
          
            if obj.username in usrlst:
                return HttpResponse('Username Already Exist')
            else:
                obj.save()
            print('Saved Successfully')
            return redirect('login')
        
    except:
        pass       
    return render(request ,'signup.html')


def login(request):
    if request.method =='POST':
        username = request.POST.get('username')                             
        password = request.POST.get('pass')
        user = authenticate(username=username,password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request,'login.html',{'error':'Invalid username or password'})
    else:
        return render(request,'login.html')
