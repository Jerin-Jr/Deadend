from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from. models import doctor
from.forms import bookingform,feedbackform
import razorpay
from deadend.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY



def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')

def booking(request):
    if request.method == ("POST"):
        form = bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conform.html')
    form= bookingform
    dict_form={'form':form}
    return render(request,'booking.html',dict_form)
def doctors(request):
    dict_doc= {'doc': doctor.objects.all()}
    return render(request,'doctors.html',dict_doc)

def feedback(request):
    if request.method == ("POST"):
        form = feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'feedbackconform.html')

    form = feedbackform
    dict_form={'form':form}    
    return render(request,'feedback.html',dict_form)
def signup(request):
    if request.method == ("POST"):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        my_user = User.objects.create_user(username=username,email=email,password=password)
        my_user.save()
        return redirect('login')
    return render(request,'signup.html')
def loginn(request):
    if request.method == ("POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Username is invalid')
    return render(request,'login.html')

# Create your views her
        
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def payment(request):
    order_amount = 50000
    order_currency = 'INR'
    payment_order = client.order.create(dict(amount=order_amount,currency=order_currency,payment_capture= 1))
    payment_order_id = payment_order['id']
     
    context = {
        'amount':500, 'api_key': RAZORPAY_API_KEY , 'order_id':payment_order_id

    }
    
        
    return render(request,'payment.html',context)

def about(request):
    return render(request,'about.html')