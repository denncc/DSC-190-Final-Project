from django.shortcuts import render
import requests
from subprocess import run, PIPE
import sys


def button(request):
    return render(request, "index.html")


def output(request):


    data  = requests.get("https://reqres.in/api/users")

    print(data.text)

    data = data.text

    return render(request, "index.html", {"data": data})
    

def external(request):
    input = request.POST.get("gameDuration")

    out = run(sys.executable, '')