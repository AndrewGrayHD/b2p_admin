from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from users.models import auth_stb01
from django.contrib.auth.models import User
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            
            if user is not None:
                user_data=User.objects.filter(username=username).first()
                auth=auth_stb01.objects.filter(username=user_data.id).first()
                try:
                    if auth.account_type in [1,2]:
                        request.session['username'] = username
                        login(request, user)
                        return redirect("/")
                    else:
                        msg = 'Please contact system administrator for access activation.'    
                except Exception as ex:
                    msg = 'Please contact system administrator for access activation.'
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'

    return render(request, "users/login.htm", {"form": form, "msg" : msg})

