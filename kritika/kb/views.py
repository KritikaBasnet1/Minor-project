from django.shortcuts import render,redirect
from . models import userinfo
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render (request,'index.html')
def mainpage(request):
    return render (request,'main.html')


def features(request):
    return render(request,'features.html')

def whytochoose(request):
    return render(request,'whytochoose.html')

def client(request):
    return render(request,'client.html')

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
def revenue(request):
    return render(request,'revenue.html')
def useractivity(request):
    return render(request,'useractivity.html')
def vehiclecatagory(request):
    return render(request,'vehiclecatagory1.html')
def base(request):
    return render(request,'base.html')

def users(request):
    userlist= User.objects.all()
    return render(request,'users.html',{'userlist':userlist})



@login_required()
def mainpage(request):
        return render(request, 'main.html')

def signuppage(request):
    try:
        if request.method == "POST":
            obj = userinfo()
            obj.username = request.POST.get('username')
            print(obj.username)
            obj.number = request.POST.get('number')
            print(obj.number)
            obj.email = request.POST.get('email')
            print(obj.email)
            obj.password = request.POST.get('pass')
            print(obj.password)
            obj.confirm_password= request.POST.get('confirm_password')
            print(obj.confirm_password)
            
            usrlst = userinfo.objects.values_list('username',flat=True)
            # print(usrlst)
            if obj.username in usrlst:
                return HttpResponse('Username Already Exist')
            else:
                obj.save()
            print('Saved Successfully')
            return redirect('login')
        
    except:
        pass       
    return render(request ,'signup.html')

def loginpage(request):
                           
   
    if request.method =='POST':
        x = request.POST.get('username')                             
        y = request.POST.get('password')                          
        z = userinfo.objects.get(username=x)
        print(z.password)
        if y==z.password:
            return redirect('main')
            
        else:
            return HttpResponse('Invalid Password')
        
    return render(request ,'login.html')


        


        

@login_required()
def new(request):
    return render(request,'new.html')




    
