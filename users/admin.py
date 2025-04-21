from django.contrib import admin

# Register your models here.
from .models import UserRegistrationModel
list_display = ('name', 'loginid', 'password', 'mobile', 'email', 'locality', 'address', 'city', 'state', 'status')
admin.site.register(UserRegistrationModel)
from django.contrib import admin
from .models import Book, Review

admin.site.register(Book)
admin.site.register(Review)
