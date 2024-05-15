from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth_auth
#from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from care.models import Pharmmodels
from .models import Boxes
from django.shortcuts import render, redirect
import json
from django.http import JsonResponse

from django.contrib import messages

from django.urls import reverse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from pharm_app import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
#from .forms import ImageForm

# Create your views here.

def index(request):
    '''
    details = "Talk to your pharmacist about your medications"  
    detail2 = "Monitor your vitals in the community pharmacy near you"
    detail3 = "Pharmacist are always accessible, talk to one today"
    
    box1 = Boxes.objects.create(details=details)
    box2 = Boxes.objects.create(details=detail2)
    box3 = Boxes.objects.create(details=detail3)
   
    detail4 = "Talk to your pharmacist about your sexual health today"
    detail5 = "Talk to your pharmacist before using those skincare products"
    detail6 = "Make sure you ask your pharmacist all drug related questions before leaving the pharmacy"
    box4 = Boxes.objects.create(details=detail4)
    box5 = Boxes.objects.create(details=detail5)
    box6 = Boxes.objects.create(details=detail6)
     '''
    boxes = Boxes.objects.all()
    
    

    pharm = Pharmmodels.objects.all()
    current_user = request.user
    username = current_user.username
    return render(request, 'patients/index.html', {'pharm': pharm, 'boxes': boxes})

@csrf_exempt    
def signup(request):
   
    if request.method == 'POST':
        #name = request.POST['name']
        name = request.POST.get('name', False)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            
            if len(password) < 6:
                messages.info(request, 'Password too short')
                return render(request, 'patients/pharmlogin.html')
            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username.")
                return render(request, 'patients/pharmlogin.html')
    
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email Already Registered!!")
                return render(request, 'patients/pharmlogin.html')
            
            if len(username)>20:
                messages.error(request, "Username must be under 20 charcters!!")
                return render(request, 'patients/pharmlogin.html')
            
            
            
            if not username.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                return render(request, 'patients/pharmlogin.html')
            

            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            
            #pharmmodel.save()
            print(request.user)
            user.username = username
            user.email = email
            
            # myuser.is_active = False
            #user.is_active = False
            user.save()
            '''
            messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
            
            # Welcome Email
            subject = "Welcome to pharm app Login!!"
            message = "Hello " + user.username + "!! \n" + "Welcome to pharm app \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You"        
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            
            # Email Address Confirmation Email
            current_site = get_current_site(request)
            email_subject = "Confirm your Email  Login!!"
            message2 = render_to_string('email_confirmation.html',{
                
                'name': user.username,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
            email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [user.email],
            )
            email.fail_silently = True
            email.send()
            '''
            
            return redirect('patients:login')
            
                                       

    return render(request, 'patients/signup.html')
'''
@csrf_exempt
def uploadimage(request, pk):
    image_location = Pharmmodels.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form_image = form.cleaned_data['pharm_image']
            image_location.pharm_image = form_image
            Pharmmodels.save()
            redirect('patients:login')
    else:
        form = ImageForm()
    return render(request, "patients/upload.html", {"form": form} )

'''

@csrf_exempt
def pharmverify(request):
   
    if request.method == 'POST':
        name = request.POST.get('name', False)
        #name = request.POST['name']
        title = request.POST.get('title', False)
        #title = request.POST['title']
        username = request.POST.get('username', False)
        #username = request.POST['username']
        email = request.POST.get('email', False)
        #email = request.POST['email']
        password = request.POST['password']


        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            
            if len(password) < 6:
                messages.info(request, 'Password too short')
                return render(request, 'patients/pharmlogin.html')
            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username.")
                return render(request, 'patients/pharmlogin.html')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email Already Registered!!")
                return render(request, 'patients/pharmlogin.html')
            
            if len(username)>20:
                messages.error(request, "Username must be under 20 charcters!!")
                return render(request, 'patients/pharmlogin.html')
        
            
            
            if not username.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                return render(request, 'patients/pharmlogin.html')
            if title.upper() != 'PHARMACIST':
                messages.error(request, "you have to be a pharmacist to signup here, thank you")
                return render(request, 'patients/pharmlogin.html')


            

            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            #user.is_active = False
            user.save()
            

            pharmmodel = Pharmmodels.objects.create(name=name, title=title, created_by=user, username=username)
            #pharmmodel.save()
            print(request.user)
            pharmmodel.name = name
            pharmmodel.title = title
            
            
            #pharmmodel.is_active = False
            pharmmodel.save()
            '''
            messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
            
            # Welcome Email
            subject = "Welcome to pharm app Login!!"
            message = "Hello " + pharmmodel.title + " " + pharmmodel.name + "!! \n" + "Welcome to pharm app \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You"        
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            
            # Email Address Confirmation Email
            current_site = get_current_site(request)
            email_subject = "Confirm your Email  Login!!"
            message2 = render_to_string('email_confirmation.html',{
                
                'name': pharmmodel.name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(pharmmodel.pk)),
                'token': generate_token.make_token(pharmmodel)
            })
            email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [email],
            )
            email.fail_silently = True
            email.send()
            '''
            #form = ImageForm()
            #return render(request, "patients/upload.html", {"form": form, "pharmodel": pharmmodel} )
            return redirect('patients:login')
                                    

    return render(request, 'patients/pharmlogin.html')


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')


@csrf_exempt
def login(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = auth_auth(request, username=username, password=password)
          if user is not None:
                
                auth_login(request, user)
                return redirect('patients:index')
                ...
          else:
                
            messages.error(request, "your username or password is incorrect")
            return render(request, "patients/login.html")
     return render(request, "patients/login.html")
          
          

@csrf_exempt
@login_required
def search(request):
    if request.method == 'POST':
        search_str = request.POST['searchpharm']
        name = Pharmmodels.objects.filter(
            name__iexact=search_str) | Pharmmodels.objects.filter(
            username__iexact=search_str) 
            
        return render(request, 'patients/search.html', {"name": name})
    


def logout(request):
        auth_logout(request)
        return redirect('/login/')




