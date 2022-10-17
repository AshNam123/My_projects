from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import service,query,answer,contact
from django.contrib.auth import authenticate,login,logout
from . forms import edit_service,edit_query
# Create your views here.
def home(request):
    service_all = service.objects.all()
    query_all = query.objects.all()
    context = {'services':service_all,'queries':query_all}
    return render(request,'blog/home.html',context)
def contact(request):
    if request.method == "POST":
        user_nm = request.POST.get('msg_name')
        email = request.POST.get('msg_email')
        message = request.POST.get('msg_message')
        con = contact(user_nm = user_nm,email = email,msg= message,user_contact_id = request.user)
        con.save()
        messages.success(request,'Your Message has been send')
        return redirect('/')
    return render(request,'blog/contact.html')
def Service(request):
    all_serrvices = service.objects.all()
    all_query = query.objects.all()
    context = {'services':all_serrvices}
    if request.method=="POST":
        service_nm = request.POST.get('servicename')
        service_pro =request.POST.get('serviceprovider')
        Contact = request.POST.get('contactnumber')
        Cost = request.POST.get('serviceprice')
        ser = service(service_name=service_nm,service_provider=service_pro,service_contact=Contact,service_cost=Cost,user_id_ser=request.user)
        ser.save()
        messages.success(request,'POST has been posted sucessfully')
        return redirect('service')
    return render(request,'blog/service.html',context)
def Query(request):
    all_query   = query.objects.all()
    all_answer = answer.objects.all()
    context = {'queries':all_query,'ans':all_answer}
    if request.method=="POST":
        query_cat = request.POST.get('querycategory')
        query_que = request.POST.get('querydetails')
        quer = query(query_category=query_cat,query_question=query_que,user_id_query = request.user)
        quer.save()
        messages.success(request,'Query has been posted')
    return render(request,'blog/query.html',context)
def user_signup(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=name).exists():
            messages.warning(request,'Username already taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email already present')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=name,email=email,password=password)
            user.save()
            messages.success(request,"User Signup Sucessfull")
            return redirect('login')
    return render(request,'blog/signup.html')
def user_login(request):
    if request.method=="POST":
        username = request.POST.get('user_name')
        password = request.POST.get('user_pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'LOGIN Sucessful')
            return redirect('/')
        else:
            messages.warning(request,'User is not registered')
            return redirect('signup')
    return render(request,'blog/login.html')
def user_logout(request):
    logout(request)
    return redirect('/')
def About(request):
    return render(request,'blog/about.html')
def details(request):
    all_query = query.objects.all()
    all_answer = answer.objects.all()
    if request.method == 'POST':
        ans = request.POST.get('answer')
        uni = request.POST.get('unique')
        ans_str = answer(ans_query = ans,unique_id = uni)
        ans_str.save()
        messages.success(request,'Answer has been sucessfully Posted')
    return render(request,'blog/detail.html')
def delete(request,id):
    all_service = service.objects.get(id=id)
    all_service.delete()
    messages.success(request,"service has been deleted")
    return redirect('/')
def delete1(request,id):
    all_query = query.objects.get(id=id)
    all_query.delete()
    messages.success(request,"Query has been deleted")
    return redirect('/')
def edit(request,id):
    all_service = service.objects.get(id=id)
    editservice = edit_service(instance=all_service)
    if request.method == 'POST':
        form = edit_service(request.POST,instance=all_service)
        if form.is_valid():
            form.save()
            messages.success(request,'Service has been updated')
            return redirect('/')
    return render(request,'blog/edit_service.html',{'edit_service':editservice})
def edit1(request,id):
    all_query = query.objects.get(id=id)
    editquery = edit_query(instance=all_query)
    if request.method == 'POST':
        form  = edit_query(request.POST,instance=all_query)
        if form.is_valid():
            form.save()
            messages.success(request,'Query has been updated')
            return redirect('/')
    return render(request,'blog/edit_query.html',{'edit_query':editquery})
