from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Bankapp.models import UserDetails


def index(request):
    return render(request, 'index.html')


def userdb(request):
    if request.method == 'POST':
        obj = UserDetails(fname=request.POST.get('First Name'),
                          lname=request.POST.get('Last Name'),
                          age=request.POST.get('Age'),
                          ph=request.POST.get('Phone'),
                          mailid=request.POST.get('Email'),
                          usname=request.POST.get('Username'),
                          pawd=request.POST.get('Password')
                          )
        obj.save()
        return render(request, 'login.html')
    return render(request, 'Registration.html')


def login(request):
    utype = request.POST.get('utype')
    uname = request.POST.get('uname1')
    pwd = request.POST.get('pwd')
    print(uname, pwd)
    if request.method == 'POST':

        if utype == 'User':
            try:
                if UserDetails.objects.get(usname=uname) is not None:
                    ak = UserDetails.objects.get(usname=uname)
                    if pwd == ak.pawd:
                        request.session['sid'] = ak.usname
                        a = request.session['sid']
                        print(a)
                        # request.method='GET'
                        return redirect('/registration/')
                    else:
                        return HttpResponse("Incorrect Password")
            except:
                return HttpResponse("username doesn't exist")
    return render(request, 'login.html')
