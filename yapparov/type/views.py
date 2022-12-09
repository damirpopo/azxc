from django.shortcuts import render
from django.http import HttpResponse
from .forms import crer
from .models import cre





def index(request):
   return render(request, "index.html",)

def cre(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        subtile = request.POST.get("subtile", "")
        URL = request.POST.get("URL", "")
        return HttpResponse(f"<div>{title}</div><br><div>{subtile}</div><br><img src='{URL}'>")
    else:
        form = crer()
        return render(request, "cre.html", {"form": form})


    
