from django.contrib import admin
from .models import WebUser
from .models import DeleteUser
# Register your models here.
admin.site.register(WebUser)
admin.site.register(DeleteUser)
