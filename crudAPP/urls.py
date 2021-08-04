from django.urls import path
from . import views
urlpatterns = [
    # path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    # path('admin', views.admin, name='admin'),
    
    #-----------------> User urls 
    path('', views.index, name='index'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('check_login', views.check_login, name='check_login'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('signupData', views.signupData, name='signupData'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    
    #-----------------> Admin Urls
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_check_login', views.admin_check_login, name='admin_check_login'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    
    #------------------> Admin Dashboard check links
    path('checkall', views.checkall, name='checkall'),
    path('pending_checkall', views.pending_checkall, name='pending_checkall'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('approved_user', views.approved_user, name='approved_user'),

]