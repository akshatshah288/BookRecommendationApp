import os
from django.conf import settings
from django.shortcuts import render, redirect
from .models import UserRegistrationModel
from django.contrib import messages

def UserRegisterActions(request):
    if request.method == 'POST':
        user = UserRegistrationModel(
            name=request.POST['name'],
            loginid=request.POST['loginid'],
            password=request.POST['password'],
            mobile=request.POST['mobile'],
            email=request.POST['email'],
            locality=request.POST['locality'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            status='waiting'
        )
        user.save()
        messages.success(request,"Registration successful!")
    return render(request, 'UserRegistrations.html') 


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                data = {'loginid': loginid}
                print("User id At", check.id, status)
                return render(request, 'users/UserHomePage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})

def UserHome(request):
    return render(request, 'users/UserHomePage.html', {})


def index(request):
    return render(request,"index.html")


import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import UserRegistrationModel

otp_storage = {}  # Temporary dictionary to store OTPs

def send_otp(email):
    otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
    otp_storage[email] = otp

    subject = "Password Reset OTP"
    message = f"Your OTP for password reset is: {otp}"
    from_email = "saikumardatapoint1@gmail.com"  # Change this to your email
    send_mail(subject, message, from_email, [email])

    return otp

def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if UserRegistrationModel.objects.filter(email=email).exists():
            send_otp(email)
            request.session["reset_email"] = email  # Store email in session
            return redirect("verify_otp")
        else:
            messages.error(request, "Email not registered!")

    return render(request, "users/forgot_password.html")

def verify_otp(request):
    if request.method == "POST":
        otp_entered = request.POST.get("otp")
        email = request.session.get("reset_email")

        if otp_storage.get(email) and str(otp_storage[email]) == otp_entered:
            return redirect("reset_password")
        else:
            messages.error(request, "Invalid OTP!")

    return render(request, "users/verify_otp.html")

def reset_password(request):
    if request.method == "POST":
        new_password = request.POST.get("new_password")
        email = request.session.get("reset_email")

        if UserRegistrationModel.objects.filter(email=email).exists():
            user = UserRegistrationModel.objects.get(email=email)
            user.password = new_password  # Updating password
            user.save()
            messages.success(request, "Password reset successful! Please log in.")
            return redirect("UserLoginCheck")

    return render(request, "users/reset_password.html")




# bookhive

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Review
from .forms import BookForm, ReviewForm
from django.db.models import Q

def home(request):
    return render(request, 'users/home.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'users/add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'users/book_list.html', {'books': books})

def book_list1(request):
    books = Book.objects.all()
    return render(request, 'users/book_list1.html', {'books': books})


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'users/edit_book.html', {'form': form, 'book': book})

def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book_list')
    else:
        form = ReviewForm()
    return render(request, 'users/add_review.html', {'form': form, 'book': book})



from django.shortcuts import render
from .models import Book
from django.db.models import Q



def filter_books(request):
    genre_query = request.GET.get('genre', '')
    books_by_genre = (
        Book.objects.filter(genre__icontains=genre_query).order_by('genre')
        if genre_query else None
    )

    author_query = request.GET.get('author', '')
    books_by_author = (
        Book.objects.filter(author__icontains=author_query).order_by('author')
        if author_query else None
    )

    return render(request, 'users/filter_books.html', {
        'books_by_genre': books_by_genre,
        'books_by_author': books_by_author,
        'genre_query': genre_query,
        'author_query': author_query,
    })


from django.shortcuts import get_object_or_404, redirect
from .models import Book

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')  # Make sure this matches your book list page name




from .models import Book, Favorite

def add_to_favorites(request, book_id):
    book = Book.objects.get(id=book_id)
    Favorite.objects.get_or_create(book=book)
    return redirect('favorite_books')  # or any page you want

def favorite_books(request):
    favorites = Favorite.objects.all()
    books = [fav.book for fav in favorites]
    return render(request, 'users/favorite_books.html', {'books': books})

def remove_from_favorites(request, book_id):
    Favorite.objects.filter(book_id=book_id).delete()
    return redirect('favorite_books')
