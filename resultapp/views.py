from django.shortcuts import render,redirect
from . models import ResultChecker
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse

# Create your views here.


def indexPage(request):
    return render(request,'index.html')


def resultPage(request):
    return render(request,'result.html')




def loginPage(request):
    if request.method=="POST":
        sname=request.POST.get('sname')
        pword=request.POST.get('spassword')
        
        if sname=="" or pword=="":
            return HttpResponse("All fields are required!")
        
        elif ResultChecker.objects.filter().exists():
            return render(request,'result.html',{'sname':sname})
        else:
            return redirect('index')
        
    return render(request,'login.html')



def logoutPage(request):
    logout(request)
    return redirect('index')
            
    



    
