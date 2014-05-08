from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
import os
import re


@csrf_protect
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/logs")
    else:
        html = "Failed"
    return HttpResponse(html)


def logs(request):
    username = request.user
    user_log_files = _user_log_files(str(username))
    return render_to_response("logs.html", {"filenames": user_log_files})


def show_log(request, filename):
    filename = "/Users/aditirav/Projects/" + filename
    with file(filename) as f:
        content = f.readlines()
    return render_to_response("log_show.html", {"content": content})


def _user_log_files(username):
    #pattern = re.compile(str(username))
    pattern = re.compile("testp.py")
    filenames = os.listdir("/Users/aditirav/Projects/")
    user_log_files = [f for f in filenames if pattern.search(f)]
    return user_log_files
