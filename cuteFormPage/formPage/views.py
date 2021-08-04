from django.shortcuts import render
from formPage import forms
from formPage.forms import userSignup,userProfileInfoForm,userForm

#for Login
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def index(request):
    return render(request,'index.html')

def basePage(request):
     return render(request,'formPage/base.html')

def signupPage(request):
    form = forms.userSignupForm()

    if request.method == 'POST':
        form = forms.userSignupForm(request.POST)

    if form.is_valid():
        print('form is valid')
        form.save(commit = True)
        return index(request)

    return render(request , 'formPage/form.html' , {'form' : form})

@csrf_protect
def user_login(request):

    if request.method == 'POST':
        # get username and password
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate the username
        user = authenticate(username = username , password = password)

        #if there is a user
        if user:
            if user.is_active:
                # login the user and send them back to index
                login(request , user)
                return render(request,'index.html')

            # if the user is not active
            else:
                return HttpResponse('user is not active')

        # if there is no user
        else:
            print('someone is trying to get in')
            print('with username:{} and password:{}'.format(username,password))
            return HttpResponse('invalid login details')

    # if the method is not POST
    else:
        return render(request,'formPage/login.html',{})

#login required
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

#special Page
@login_required
def special(request):
    return HttpResponse('you are logged in, Nice!')

def registerPage(request):

    registered = False

    if request.method == 'POST':
        user_form = userForm(data = request.POST)
        profile_form = userProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():


            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.picture = request.FILES['profile_pics']

                profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = userForm()
        profile_form = userProfileInfoForm()

    return render(request , 'formPage/registeration.html',
                            {'user_form' : user_form ,
                             'profile_form' : profile_form ,
                             'registered':registered })
