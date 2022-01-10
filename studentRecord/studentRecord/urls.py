"""studentRecord URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.details,name='details'),
    path('loginPage/',views.loginPage,name='loginPage'),
    #authenticate user
    path('authenticate/',views.login,name='authenticate'),
    #form for accepting the data for student 
    path('create/',views.create,name='create'),
    path('createUser/',views.createUser,name='createUser'),
    #to display the data of all students
    path('details/',views.details,name='details'),
    path('details/<username>',views.detailsname,name='detailsname'),
    #to get data for perticular user on clicking on the name
    path('detailsUsers/<ids>',views.detailsUsers,name='detailsUsers'),
    #for deleting the user
    path('delete/<ids>',views.delete,name='delete'),
    #for update the user
    path('update/<int:ids>',views.update,name='update'), 
     path('logouts/',views.logouts,name='logouts'),
    #form for submitting the url
    path('senturl/',views.sentUrl),
    path('signupPage/',views.signupPage,name='signupPage'),
    path('stsearch/',views.searchName,name='searchName'),
    path('urls/',views.url),
    path('signup/',views.signup),
    path('changePage/<username>',views.changePage),
    path('changePassword/',views.changePassword,name='changePassword')
    
    
]
