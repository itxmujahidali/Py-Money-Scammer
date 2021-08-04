from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.http import HttpResponse
from crudAPP.models import WebUser

# Create your views here.

def index(request):
    # if request.session.has_key('is_logged'):
        return render(request, 'users/index.html')
    # else:
        # return render(request,'users/user_login.html')
        

def user_login(request):
    return render(request, 'users/user_login.html')

def check_login(request):
#------------->  Login logic 
    if (request.method == 'POST'):
        login_email = request.POST ['login_email']
        login_password = request.POST ['login_password']

        #Compare with Database where input email exist!
        try:
            CheckUser = WebUser.objects.get(Email=login_email)
        except:
            messages.error(request, "User Dosen't Exist!")
            return render(request, 'users/user_login.html')
        if (CheckUser.status == True):
            if (login_email == CheckUser.Email and login_password == CheckUser.Password):
                # FirstName = CheckUser.firstName
                # LastName = CheckUser.lastName
                # name = {'name':'Welcome ' + FirstName + ' ' + LastName}
                request.session['is_logged'] = True
                return render(request, 'users/index.html')
            else:
                messages.error(request, 'Your Email or Password is incorrect! ')
                return render(request, 'users/user_login.html')
        else:
            messages.warning(request, 'Your Request Still Pending!')
            return redirect ('user_login')
    else:
        return render(request, 'users/index.html')
#----------------> END Login logic

#----------------> LOGOUT Logic
def user_logout(request):
    del request.session['is_logged']
    return render(request, 'users/user_login.html')
#----------------> END LOGOUT Logic

def user_signup(request):
    return render(request, 'users/user_signup.html')

def aboutus(request):
    if request.session.has_key('is_logged'):
        return render(request, 'users/aboutus.html')
    else:
        return render(request,'users/user_login.html')
    

def contactus(request):
    if request.session.has_key('is_logged'):
        return render(request, 'users/contactus.html')
    else:
        return render(request,'users/user_login.html')

def admin_login(request):
    return render(request, 'admin/admin_login.html')

def admin_check_login(request):
#------------->  Login logic 
    if (request.method == 'POST'):
        login_email = request.POST ['getadminemail']
        login_password = request.POST ['getadminpassword']

        #Compare with Database where input email exist!
        try:
            CheckUser = WebUser.objects.get(Email=login_email)
        except:
            messages.error(request, "User Dosen't Exist!")
            return render(request, 'users/admin_login.html')
        if (CheckUser.isAdmin == True):
            if (login_email == CheckUser.Email and login_password == CheckUser.Password):
                request.session['is_logged'] = True
                #check Approved users
                total_approved_request = len(WebUser.objects.filter(status=True))
                #check Pending users
                pending_request = len(WebUser.objects.filter(status=False))
                admin_tick_pending_request = len(WebUser.objects.filter(isAdmin=True))
                #check total users
                total_users =  len(WebUser.objects.all()) - admin_tick_pending_request
                
                context = {
                    'total_pending_request':pending_request,
                    'total_approved_request':total_approved_request,
                    'total_users':total_users,
                }
                return render(request, 'admin/admin_dashboard.html',context)
            else:
                messages.error(request, 'Your Email or Password is incorrect! ')
                return render(request, 'admin/admin_login.html')
        else:
            messages.warning(request, 'Sorry! You are not Admin')
            return render(request, 'admin/admin_login.html')
    else:
        return HttpResponse('Something Went Wrong! ')
#----------------> END Login logic

def admin_dashboard(request):
    return render(request,'admin/admin_dashboard.html')


def signupData(request):
#------------->  signup logic 
    if request.method == 'POST':
        firstname = request.POST ['firstname']
        lastname = request.POST ['lastname']
        fathername = request.POST ['fathername']
        username = request.POST ['username']
        email = request.POST ['email']
        password = request.POST ['password']
        #Sending HTML-Data to Model for store into Database!
        #Creating class object
        User = WebUser(firstName = firstname, lastName = lastname, fatherName = fathername, userName = username, Email = email, Password = password)
        User.save()
        return render (request, 'users/user_signup.html')
    else:
        return HttpResponse ('404 - Error')
#----------------> END signup logic

def checkall(request):
    data = WebUser.objects.filter(isAdmin=False)
    length = len(data)
    context = {
        'data': data,
        'length' : length
    }
    return render(request, "admin/checkall.html",context)

def pending_checkall(request):
    data = WebUser.objects.filter(status=False)
    context = {
        'data': data
    }
    return render (request, 'admin/checkall.html',context)

def delete_user(request,username):
    return HttpResponse(username)

def approved_user(request):

    return HttpResponse('User has been approved!')