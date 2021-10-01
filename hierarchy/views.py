from django.shortcuts import render, HttpResponseRedirect, reverse
from hierarchy.models import Hierarchy
from hierarchy.forms import MyFilesForm, LoginForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def index(request):
    template_name = "index.html"
    clans = Hierarchy.objects.all()
    union = {"clans": clans}
    return render(request, template_name, union)

def add_form(request):
    if request.method == "POST":
        form = MyFilesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            parent = Hierarchy.objects.create(
                name=data.get("name"),
                parent=data.get("parent")
            )
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = MyFilesForm()

    return render(request, "generic.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if user:
                login(request,user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
    
    form = LoginForm()
    return render(request, "generic.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
                   