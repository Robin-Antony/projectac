from django.shortcuts import render,redirect
from. forms import OrderCreationForm,MyUserCreationForm,StaffRegisterForm,UserPasswordResetForm,StaffUpdateForm,FeedbackForm,QandAForm
from. models import Order,Rating,AccurOrder,User,Feedback,QandA
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout,get_user_model
from django.template.loader import render_to_string
from.token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage
import json
from django.http import JsonResponse

# Create your views here.

def index(request):
    ratings = Rating.objects.all()[:10]
    rating_value = 0
    total_rating = 0
    orders = Order.objects.filter(complete=True)
    form = QandAForm()
    answers = QandA.objects.filter(answered=True)[:10]
    for rating in ratings:
        total_rating += 1
        rating_value += rating.rated 

    try:
        average_rating = rating_value/total_rating
    except:
        average_rating = 0
    
    if request.method == 'POST':
        form = QandAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context={'ratings':ratings,'average_rating':average_rating,'total_rating':total_rating,'form':form,'answers':answers}
    return render(request,'base/index.html',context)

def activateEmail(request,user,to_email):
    mail_subject = "Activate your user account"
    message = render_to_string("base/template_activate_account.html", {

        'user':user.first_name,
        'domain':get_current_site(request).domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
        "protocol":'https' if request.is_secure()else 'http'
    }
        
    )
    email = EmailMessage(mail_subject,message,to=[to_email])
    if email.send():
        messages.success(request,f'Dear user please go to your email and click on recived activation link to confirm and complete the registration')
    else:
        messages.error(request,'Problem in sending e-mail to --')



def userRegister(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = user.first_name.lower()
            user.last_name = user.last_name.lower()
            user.is_active = False
            user.save()
            activateEmail(request,user,request.POST.get('email'))
       
    context = {'form':form}
    return render(request,'base/user_register.html',context)


def activate(request,uidb64,token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active =True
        user.save()
        messages.success(request,'thank you for your email confermation now you can login to your account')
        return redirect('login_page')
    else:
        messages.error(request,'Activation link is invalid')
        return redirect('index')

def passwordResetEmail(request,user,to_email):
    mail_subject = "Reset Your password"
    message = render_to_string("base/template_reset_password.html", {

        'user':user.first_name,
        'domain':get_current_site(request).domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
        "protocol":'https' if request.is_secure()else 'http'
    }
        
    )
    email = EmailMessage(mail_subject,message,to=[to_email])
    if email.send():
        messages.success(request,f'Dear user please go to your email and click on recived  link to reset your password')
    else:
        messages.error(request,'Problem in sending e-mail to --')


def passwordReset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            
        except:
            user = None
        if user is not None:
            passwordResetEmail(request,user,email)
        else:
            messages.error(request,'No User with this email id')
            return redirect('user_register')
    

    return render(request, 'base/password_reset.html')

def reset(request,uidb64,token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print('user is :', user)
    except:
        user = None
    form = UserPasswordResetForm()
    print('token :',account_activation_token.check_token(user,token))
    if user is not None and account_activation_token.check_token(user,token):
        print('user is :', user)
        if request.method == 'POST':
            print('user is :', user)
            form = UserPasswordResetForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data.get('password1')
                user.set_password(password)
                user.save()

                messages.success(request,'Thank you for your email confirmation now you can login to your account')
                return redirect('login_page')
    else:
        messages.error(request,'Activation link is invalid')

    context={'form':form}
    return render(request,'base/reset.html',context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            user = None
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('order_page')
            else:
                return redirect('index')
        else:
            messages.error(request, 'Invalid user credentials')

    return render(request,'base/login.html')



def order(request):
    form = OrderCreationForm()
    if request.method == 'POST':
        name= request.POST.get('name').lower()
        name= name.strip(" ")
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        problem = request.POST.get('problem')
        try:
            order = Order.objects.get(name=name,phone=phone)

        except:
            order = None
            print(order)
            Order.objects.create(
                name=name,
                phone=phone,
                address=address,
                problem=problem,
                order_no = 1
                )
            
        if order is not None:
            if order.complete or order.order_no > 1:
                try:
                    accurorder = order.accurorder
                    accurorder.delete()
                except:
                    accurorder = None

                # order.order_no += 1
                order.complete = False
                order.accured = False
                order.accured_by = None
                order.address=address
                order.problem=problem
                order.save()
                
            else:
                order_numb = order.order_no
                order.delete()
                try:
                    accepted_order = AccurOrder.objects.get(order=order)#if there is more than one accepted order an error occur (get())
                    accepted_order.delete()
                except:
                    accepted_order = None

                
                Order.objects.create(
                name=name,
                phone=phone,
                address=address,
                problem=problem,
                order_no = 1
                )
        return redirect('index')

    context = {'form':form}

    return render(request,'base/address_form.html',context)


@login_required(login_url = 'user_register')
def orderPage(request):
    user = request.user
    if user.is_staff:
        orders = Order.objects.all()[:10]
        open_orders = Order.objects.filter(accured=False)
    else:
        orders = []
        open_orders = []
    if request.method == 'POST' and user.is_staff:
        order_id = request.POST.get('order')
        order = Order.objects.get(id=order_id)
        try:
            accur_order = AccurOrder.objects.get(order=order)
        except:
            AccurOrder.objects.create(staff=user,order=order)
            order.accured = True
            order.accured_by = user
            order.save()
        return redirect('order_page')
        
    
    context = {'orders':orders,"open_orders":open_orders, 'staff':user}
    return render(request,'base/order_page.html',context)


@login_required(login_url = 'user_register')
def staffRegister(request):
    form = StaffRegisterForm()
    
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        document = request.FILES.get('documents')
        phone = request.POST.get('phone')
        user = request.user
        user.avatar=avatar
        user.documents = document
        user.phone = phone
        user.save()

        return redirect('staff_profile',pk=user.id)

    context = {'form':form}
    return render(request,'base/staff_register.html',context)

def editProfile(request):
    user = request.user
    
    form = StaffUpdateForm(instance=user)
    print('user name is :',form)
    if request.method == 'POST':
        form = StaffUpdateForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('staff_profile',pk=user.id)
    context = {'form':form}
    
    return render(request,'base/edit_profile.html',context)
    


@login_required(login_url = 'user_register')
def staffProfile(request,pk):
    user = User.objects.get(id=pk)
    rating_value = 0
    total_rating = 0
    if user.is_staff == False:
        return redirect('index')
    if user.is_staff:
        accepted_orders = user.accurorder_set.all()
        # completed_orders = accepted_orders.filter(complete=True)
        # print('completed orders : ', completed_orders)
        ratings = user.rating_set.all()
    else:
        accepted_orders = []
        ratings = []

    for rating in ratings:
        total_rating += 1
        rating_value += rating.rated 

    try:
        average_rating = rating_value/total_rating
    except:
        average_rating = 0

    if request.method == "POST":
        order_id = request.POST.get('order_id')
        price = float(request.POST.get('order_price'))
        history = request.POST.get('history')

        try:
            order = Order.objects.get(id=order_id)
            order.order_price += price
            order.complete=True
            order.order_no += 1
            order.history += "   " + history
            order.save()
        except:
            order = None
        return redirect('staff_profile',pk=pk)
    context = {'staff':user,'accepted_orders':accepted_orders, 'ratings':ratings,'average_rating':average_rating,'total_rating':total_rating}
    return render(request, 'base/staff_profile.html',context)

def orderStatus(request):
    order=None      
    if request.method == 'POST':
        name = request.POST.get('name').lower()
        phone = request.POST.get('phone')
        name= name.strip(" ")
        try:
            order = Order.objects.get(name=name,phone=phone)
        except:
            order = None
        if order != None and order.complete == True:
            pk = order.id
            return redirect('rating',pk=pk,phone=phone)
        elif order != None:
            messages.error(request,'Your order is not completed yet')
        else:
            messages.error(request,'no orders with this name and phone number')

    context={'order':order}        
    return render(request,'base/rate_now.html',context)

def rating(request, pk, phone):
    order = Order.objects.get(id=pk)
    phone_one = order.phone
    phone_two = phone
    staff = order.accured_by
    if request.method == 'POST' and phone_one == phone_two:
        rating = (request.POST.get('ratestar'))     
        body = request.POST.get('body')
        Rating.objects.create(order=order,rated=rating,body=body,staff=staff)
        return redirect('index')

    return render(request,'base/rating.html')


def logoutPage(request):
    logout(request)
    return redirect('index')

def feedbackPage(request):
    form = FeedbackForm()


    if request.method == 'POST':
        name= request.POST.get('name')
        feedback= request.POST.get('feedback')
        Feedback.objects.create(name=name,feedback=feedback)
        return redirect('index')

    
    return render(request, 'base/feedback.html',{"form":form})

def carrierPage(request):
    return render(request,'base/carrier.html')

def privacyPolicy(request):
    return render(request,'base/privacy_policy.html')

def aboutUs(request):
    return render(request,'base/about_us.html')

def helpPage(request):
    return render(request,'base/help.html')

def termsAndConditons(request):
    return render(request,'base/terms_and_conditions.html')

def whatWeDo(request):
    return render(request,'base/what_we_do.html')

def WhyUs(request):
    return render(request,'base/why_us.html')

