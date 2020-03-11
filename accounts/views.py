# Reverse allows us to pass the name of a URLs instead of a name of a view
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationform

# Create your views here.
def index(request):
    return render(request, "index.html")


# A decorator that we can put on top of our function signature to check if the
# user is logged in before executing any more of the code 
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect(reverse('index'))

def login(request):
    # Don't want to display the login page to users that are logged in.
    # Without this if statement in, we could access the login page by entering
    # the URL into the URL bar.
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        # We're going to pass in the request post as our other constructor
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('profile'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        # Create an instance of the login form
        login_form = UserLoginForm()

    # Pass that form to the template. We'll give our context dictionary and
    # that should be a string so the key is login form and the value is the
    # name of the form instance that we just created 
    return render(request, "login.html", {'login_form': login_form})


def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegistrationform(request.POST)
    
        if registration_form.is_valid():
            # As we already specified the model inside of our meta class on
            # our registration form we don't need to specify model again here 
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationform()

    return render(request, "register.html",
                  {'registration_form': registration_form})

def user_profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, "profile.html", {'profile': user})
"""
Notice the user, there's user there and profile that's because we don't
actually really need to grab a user profile from the database in this example
because all of the user information is stored in the request object however if
we were to extend this user profile and create an edit profile page where a user
could edit their email address or something and then by using a model by default 
would give us much more control but for now we can use the combination of both the
user and profile objects. The user is the standard user that are stored in the request
"""
