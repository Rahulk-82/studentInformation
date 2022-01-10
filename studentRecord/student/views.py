from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http import HttpResponse,HttpResponseRedirect
from student.serializers import StudentInfoSerializer
from student.serializers import StudentAcademicsSerializer
from rest_framework.decorators import api_view
import json
from django.shortcuts import redirect
from .serializers import StudentInfoSerializer
from .serializers import StudentAcademicsSerializer
import requests
from bs4 import BeautifulSoup
from .models import StudentInfo
from .models import StudentAcademics
from .forms import StudentForm
from django.contrib.auth.models import User

login=False
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def loginPage(request):
    
    return  render(request, 'student/login/index.html')
   
def login(request):
    name = request.POST['name']
    password = request.POST['password']
    user = authenticate(username=name, password=password)
    if user:
        return redirect('/details/'+name)
        
    else:
        return  render(request, 'student/login/index.html')
        # Redirect to a success page.
def signupPage(request):

    return render(request, 'student/login/signup.html')
    
def signup(request):
     
    name = request.POST.get('name')
    password = request.POST.get('password')
    emailid=request.POST.get('emailid')
    user = User.objects.create_user(name,emailid, password)
    user.save()
    return redirect('/details/')
def changePage(request,username):
    return  render(request, 'student/login/changepassword.html',{'user':username})
    
def changePassword(request):
    u = User.objects.get(username=request.POST['user'])
    u.set_password(request.POST['password'])
    u.save()
    return HttpResponseRedirect('/detailsname/') 

def logouts(request):
    logout(request)
    return redirect('/details/')
    
def checkLoginStatus(username):    
    if User.objects.filter(username=username).exists():
        usr = User.objects.get(username=username)
        if usr.is_authenticated:
            return True
        else:
            return False
    else:
        print("No user exist with this {} username.".format(username))
        return False   
    
def create(request):
    return render(request,'student/login/create.html')

def createUser(request):
        Rollno=request.POST['roll_no']
        Name=request.POST['name']
        Class= request.POST['class']
        School= request.POST['school']
        Mobile= request.POST['mobile']
        Address= request.POST['address']
        Maths= request.POST['maths']
        Physics= request.POST['physics']
        Chemistry= request.POST['chemistry']
        Biology=request.POST['biology']
        English= request.POST['english']
             
        studentS=StudentInfo(Rollno=Rollno,Name=Name,Class=Class,School=School,Mobile=Mobile,Address=Address)  
        studentS.save()
        studentA=StudentAcademics(Rollno=studentS,Math=Maths,Physics=Physics,Chemistry=Chemistry,Biology=Biology,English=English)
        studentA.save()
        return redirect('/details/')
        
def searchName(request):
    name=request.POST['stname']
    stud = StudentInfo.objects.filter(Name=name)
    return  render(request, 'student/login/details.html',{'user':login,'stu': stud})
    
    

def details(request):
    SI = StudentInfo.objects.all()
    SA= StudentAcademics.objects.all()
    stud=SI
    return  render(request, 'student/login/details.html',{'user':login,'stu': stud})
def detailsname(request,username):
    SI = StudentInfo.objects.all()
    SA= StudentAcademics.objects.all()
    u=StudentInfo.objects.filter(Name=username)
    s=checkLoginStatus(username)
    
    stud=SI
    if s:
        
        return  render(request, 'student/login/details.html',{'user':s,'stu': stud,'status':s,})
    else:
        stud=SI
        
        return render(request, 'student/login/details.html',{'user':s,'stu': stud,'status':s})
    
#for deleting data   
def delete(request,ids):
    reg = StudentInfo(Rollno=ids)
    reg.delete()
    SI = StudentInfo.objects.all()
    SA= StudentAcademics.objects.all()
    stud=SI
    return  render(request, 'student/login/details.html',{'stu': stud})
def update(request,ids):
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(StudentInfo, Rollno = ids)
 
    # pass the object as instance in form
    form = StudentForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/details/')
 
    # add form dictionary to context
    context["form"] = form
    
    return render(request, "student/login/update.html", context)

 
# after updating it will redirect to detail_View
 
# update view for details
    # dictionary for initial da
    
def sentUrl(request):
    return  render(request, 'student/login/findurl.html')
def url(request):
    reqs = requests.get(request.POST['urls'])
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    return  render(request, 'student/login/link.html',{'link': urls})
def detailsUsers(request,ids):
    SI = StudentInfo.objects.filter(Rollno=ids)
    SA = StudentAcademics.objects.filter(Rollno=ids)
    #s=checkLoginStatus(name)
    #if s:
    return  render(request, 'student/login/detailUser.html',{'stu': SA})
    #else:
    #return HttpResponse('<h1> NO authorized</h2>')
        
        

   
    

