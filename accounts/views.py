from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Account
from django.contrib.auth import get_user_model
from LavenderHaze.utils import send_activation_email,send_forgotpassword_mail

#for email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse
# Create your views here.

def signup(request):  
    if request.method == 'POST':
        form =   RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']

            User    =   get_user_model()
            user= User.objects.create_user(name=name,email=email,password=password)
            user.phone=phone
            user.save()
            #sending email-helper function in utils
            send_activation_email(request,user)
            messages.success(request, "We have send you an email ,please verify it")
            return redirect('/accounts/signin/?command=verification&email='+email)
    else:
        form   = RegistrationForm()
    context =   {
        'form' : form,
    }
    return render(request,'accounts/signup.html',context)


             
def signin(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('ghome')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('signup')
    return render(request,'accounts/signin.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('ghome')

def activate(request,uidb64,token):
   try:
    uid =urlsafe_base64_decode(uidb64).decode()
    user=Account._default_manager.get(pk=uid)
   except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
    user=None

   if user is not None and default_token_generator.check_token(user,token):
    user.is_active=True
    user.save()
    messages.success(request,'account activated')
    return redirect('signin')
   else:
    messages.error(request,"invalid activation link")
    return redirect('signup')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='signin')
def profile(request):
    return render(request,'accounts/profile.html') 


def forgotPassword(request):
    if request.method=='POST':
        email= request.POST['email']
        if Account.objects.filter(email=email).exists():
            user=Account.objects.get(email__iexact=email) 
            send_forgotpassword_mail(request,user,email)
            messages.success(request,"Paswword reset email has been sent")
            return redirect('signin')
        else:
            messages.error(request,"Account doesnot exist")
            return redirect('forgotPassword')
    return render(request,'accounts/forgotPassword.html')

def resetpassword_validate(request,uidb64,token):
    try:
       uid =urlsafe_base64_decode(uidb64).decode()
       user=Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
       user=None
       
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid'] = uid
        messages.success(request,"Please reset your password")
        return redirect('resetPassword')
    else:
        messages.error(request,"This link has been expired")
        return redirect('signin')
@login_required(login_url='signin')
def resetPassword(request):
    if request.method=='POST':
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            uid=request.session.get('uid')
            user=Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,"Password reset successfull")
            return redirect('signin')

        else:
            messages.error(request,"Passwords do not match")
            return redirect('resetPassword')

    else:

        return render(request,'accounts/resetPassword.html')


def edit_profile(request):
    return render(request,'accounts/edit_profile.html')