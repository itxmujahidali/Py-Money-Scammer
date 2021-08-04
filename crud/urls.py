"""crud URL Configuration

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
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/', include('crudAPP.urls')),
    # path('admin_dashboard/', include('crudAPP.urls')),
    path('', include('crudAPP.urls')),
    path('user_login', include('crudAPP.urls')),
    path('user_logout', include('crudAPP.urls')),
    path('check_login', include('crudAPP.urls')),
    path('user_signup', include('crudAPP.urls')),
    path('signupData', include('crudAPP.urls')),
    path('aboutus', include('crudAPP.urls')),
    path('contactus', include('crudAPP.urls')),
    #Admin Urls
    path('admin_login', include('crudAPP.urls')),
    path('admin_check_login', include('crudAPP.urls')),
    path('admin_dashboard', include('crudAPP.urls')),

    #Checking Dashboard links
    path('checkall', include('crudAPP.urls')),
    path('pending_checkall', include('crudAPP.urls')),
    path('delete_user', include('crudAPP.urls')),
    path('approved_user', include('crudAPP.urls')),

]
