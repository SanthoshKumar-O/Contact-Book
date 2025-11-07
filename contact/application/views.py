from django.shortcuts import render,redirect,get_object_or_404
from .models import Number
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def frontpage(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request,"application/welcome.html")

@login_required(login_url='login')
def contactbook(request):
    msg=None
    if request.method=='POST':
        name=request.POST.get("name")
        no=request.POST.get("no")
        email=request.POST.get("mail")
        add=request.POST.get("address")
        full=name.replace(" ","")
        if not name or not no:
            msg="name and no are required fields!"
        elif len(no)!=10 or not no.isdigit():
            msg="Enter valid mobile number with 10 digits"
        elif not full.isalpha():
            msg="Enter valid name for the contact"
        elif Number.objects.filter(user=request.user,number=no).exists():
            msg="Contact number already exist !"
        else:
            contact = Number(user=request.user, name=name, number=no, email=email, address=add)
            contact.save()
            return redirect('contactbook')
    return render(request,'application/first.html',{'msg':msg})

@login_required(login_url='welcome')
def home(request):
    return render(request,'application/home.html')

@login_required(login_url='login')
def listcontact(request):
    contacts=Number.objects.filter(user=request.user)
    return render(request,'application/list.html',{'contacts':contacts})

@login_required(login_url='login')
def deletecontact(request,id):
    contact=get_object_or_404(Number,id=id,user=request.user)
    contact.delete()
    return redirect('List_contact')

@login_required(login_url='login')
def searchcontact(request):
    con=request.GET.get("searchc")
    type=request.GET.get("how")
    if not con:
        contacts=Number.objects.filter(user=request.user)
    elif type=="name":
        contacts=Number.objects.filter(name__icontains=con,user=request.user)
    elif type=="number":
        contacts=Number.objects.filter(number__icontains=con,user=request.user)
    else:
        contacts=Number.objects.filter(user=request.user)
    return render(request,"application/view.html",{"contacts":contacts})

@login_required(login_url='login')
def updatecontact(request, id):
    contacts = get_object_or_404(Number, id=id, user=request.user)
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        newno = request.POST.get("number")

        if not name.strip() or not newno.strip():
            messages.error(request, "Name and number are required fields!")
            return redirect("update_contact", id=id)
        elif len(newno) != 10 or not newno.isdigit():
            messages.error(request, "Enter a valid mobile number with 10 digits!")
            return redirect("update_contact", id=id)
        elif not name.strip().isalpha():
            messages.error(request, "Enter a valid name for the contact!")
            return redirect("update_contact", id=id)
        elif Number.objects.filter(user=request.user, number=newno).exclude(id=id).exists():
            messages.error(request, "Contact number already exists!")
            return redirect("update_contact", id=id)
        else:
            contacts.name = name
            contacts.email = email
            contacts.address = address
            contacts.number = newno
            contacts.save()
            return redirect("search_contact")

    return render(request, "application/update.html", {"contacts": contacts})


def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        confirm=request.POST.get("confirm")

        if User.objects.filter(username=username).exists():
            messages.error(request,"User with this username already exists.")
            return redirect('signup')
        if password!=confirm:
            messages.error(request,"password confirmation failed!")
            return redirect("signup")
        
        User.objects.create_user(username=username,password=password)
        messages.success(request,"User created successfully. Please login!")
        return redirect("login")
    return render(request,'application/signup.html')

def loginview(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)
        if user is None:
            return render(request,'application/login.html',{"error":"Invalid username or password"})
        else:
            login(request,user)
            return redirect('home')
    return render(request,'application/login.html')

@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect('login')