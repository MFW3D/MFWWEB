"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import *
from django.core.exceptions import ObjectDoesNotExist
def userinfo(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/userinfo.html',
        {
            'title':'账户信息',
            'year':datetime.now().year,
        }
    )

def signup(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        comfirm=request.POST['comfirm']
        email=request.POST['email']
        if comfirm!=password:
             return render(
                request,
                'app/signup.html',
                {
                    'title':'Home Page',
                    'year':datetime.now().year,
                    'errors':'账户或密码错误',
                })
        usernums = User.objects.filter(username= username);
        if usernums!=0:
            return render(
            request,
            'app/signup.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
                'errors':'账户已存在',
            }
        )
        user = User.objects.create_user(username, comfirm,password)
        return render(
            request,
            'app/ok.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
            }
        )
    return render(
        request,
        'app/signup.html',
        {
            'title':'注册成为MFW3D会员',
            'year':datetime.now().year,
            'errors':'',
        }
    )


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
