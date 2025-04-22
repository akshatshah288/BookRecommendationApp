"""
URL configuration for student_hive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from book_hive import views as mainView
from admins import views as admins
from users import views as usr
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView.index, name="index"),
    path("index", mainView.index, name="index"),
    path("Adminlogin", mainView.AdminLogin, name="AdminLogin"),
    path("UserLogin", mainView.UserLogin, name="UserLogin"),

    # admin views
    path("AdminLogincheck", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path('userDetails', admins.RegisterUsersView, name='RegisterUsersView'),
    path('ActivUsers/', admins.ActivaUsers, name='activate_users'),
    path('DeleteUsers/', admins.DeleteUsers, name='delete_users'),
    path('adminhome', admins.adminhome, name='adminhome'),
    
    #userurls
    path('UserRegisterForm',usr.UserRegisterActions,name='UserRegisterForm'),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("forgot-password/",usr.forgot_password, name="forgot_password"),
    path("verify-otp/",usr.verify_otp, name="verify_otp"),
    path("reset-password/",usr.reset_password, name="reset_password"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("index/", usr.index, name="index"),
   
    #bookhive 
    path('home', usr.home, name='home'),
    path('add_book/', usr.add_book, name='add_book'),
    path('book_list/', usr.book_list, name='book_list'),
    path('book_list1/', usr.book_list1, name='book_list1'),
    path('edit_book/<int:book_id>/', usr.edit_book, name='edit_book'),
    path('add_review/<int:book_id>/', usr.add_review, name='add_review'),
    # path('filter_books/', usr.filter_books, name='filter_books'),
    path('filter/books/', usr.filter_books, name='filter_books'),
    path('delete/<int:book_id>/', usr.delete_book, name='delete_book'),
    path('add-to-favorites/<int:book_id>/', usr.add_to_favorites, name='add_to_favorites'),
    path('favorite-books/', usr.favorite_books, name='favorite_books'),
    path('remove-from-favorites/<int:book_id>/', usr.remove_from_favorites, name='remove_from_favorites'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


