from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
from CRUDApp.forms import LoginForm, ProfileForm
from CRUDApp.models import Profile, Login


def homeview(request):
    return render(request,'index.html')

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_user:
                return redirect('userhome')
            elif user.is_staff:
                return redirect('adminhome')

        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'login.html')

def adminhome(request):
    ad = Profile.objects.all()
    return render(request,'adminhome.html',{'ad':ad})

def userhome(request):
    us = Profile.objects.all()
    return render(request, 'userhome.html',{'us':us})
def userregister(request):
    login_form = LoginForm()
    user_form = ProfileForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        user_form = ProfileForm(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            w = user_form.save(commit=False)
            w.user = user
            w.save()
            messages.info(request, 'Registered Successfully')
            return redirect('userhome')
    return render(request, 'userregister.html', {'login_form': login_form, 'user_form': user_form})

def logoutview(request):
    logout(request)
    return redirect('loginview')

def profileupdate(request,id):
    su = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, instance=su)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile Updated')
            return redirect('userhome')
    else:
        form = ProfileForm(instance=su)
    return render(request, 'profileupdate.html', {'form': form})

def profiledelete(request,id):
    sd = Profile.objects.get(id=id)
    if request.method=='POST':
        sd.delete()
        return redirect('userhome')

def userdelete(request,id):
    teach = Profile.objects.get(id=id)
    t = Login.objects.get(user=teach)
    if request.method == 'POST':
        t.delete()
        messages.info(request, 'User deleted successfully')
        return redirect('adminhome')
    else:
        return redirect('adminhome')
