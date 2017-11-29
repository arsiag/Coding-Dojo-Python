# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *

# Create your views here.

def users(request):
    # print "*" * 50
    # print "inside users"
    # print "*" * 50
    return render(request,"belt_review/login.html")

def create(request):
    # print "*" * 50
    # print "inside create"
    # print "*" * 50
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error, extra_tags = 'register')
    else:
        password = request.POST['pword']
        hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=hash_pw)
        messages.success(request, "Registration was successful! You can log in now.", extra_tags ="register")
    
    return redirect("/")


def login(request):
    # print "*" * 50
    # print "inside login"
    # print "*" * 50
    email = request.POST['email']
    password = request.POST['pword']
    try:
        user = User.objects.get(email = email)
    except:
        messages.error(request, "Please enter a valid email!", extra_tags = 'login')
        return redirect("/")
    encrypted_password = user.password.encode()
    id = user.id

    if bcrypt.checkpw(password.encode(), encrypted_password):
        # messages.success(request, "login was successful! You are logged in now!", extra_tags ="login")
        request.session['id'] = user.id
        request.session['alias'] = user.alias
        return redirect("/books")
    else:
        messages.error(request, "Invalid password!", extra_tags = 'login')
        return redirect("/")
    
    return redirect("/") # in case of other situations not taken care of above
    
def home(request):
    # print "*" * 50
    # print "inside home"
    # print "*" * 50
    if request.session.get('id'):
        lastThree = Review.objects.all().order_by('-created_at')[:3]
        theRest = Review.objects.all().order_by('-created_at')[3:]
        context = {
            'recent': lastThree,
            'rest': theRest
        }
        return render(request,"belt_review/home.html", context)
    else:
        messages.error(request, "Please log in!", extra_tags = 'login')
        return redirect("/")

def logout(request):
    # print "*" * 50
    # print "inside logout"
    # print "*" * 50
    request.session.flush()
    return redirect('/')

def add(request):
    # print "*" * 50
    # print "inside add"
    # print "*" * 50
    context = {
        "authors": Author.objects.all()
    }
    return render(request,"belt_review/add.html", context)

def book_create(request):
    # print "*" * 50
    # print "inside book_create"
    # print "*" * 50
    errors = Review.objects.review_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error, extra_tags = 'book_create')
        return redirect('/books/add')
    else:
        this_review = Review.objects.review_creator(request.POST, request.session['id'])
        this_book = this_review.book
        this_bookid = this_book.id
    return redirect('/books/'+ str(this_bookid))

def show(request, id):
    # print "*" * 50
    # print "inside show"
    # print "book_id: " + str(id)
    # print "*" * 50
    context = {
        'book': Book.objects.get(id=id)
    }
    return render(request,"belt_review/book.html", context)

def show_user(request, id):
    # print "*" * 50
    # print "inside show_user"
    # print "book_id: " + str(id)
    # print "*" * 50
    user = User.objects.get(id=id)
    reviews = user.reviews_left.all()
    book_ids = reviews.values("book_id").distinct()
    books = []
    for book in book_ids:
        books.append(Book.objects.get(id=book["book_id"]))

    context = {
        'user': user,
        'books': books
    }

    return render(request,"belt_review/user.html", context)

def review_create(request, id):
    # print "*" * 50
    # print "inside review_create"
    # print "book_id: " + str(id)
    # print "*" * 50
    this_book = Book.objects.get(id=id)
    book_data = {
        'title': this_book.title,
        'author': this_book.author.id,
        'rating': request.POST['rating'],
        'review': request.POST['review'],
        'new_author': ''
    }
    errors = Review.objects.review_validator(book_data)
    if errors:
        for error in errors:
            messages.error(request, error, extra_tags = 'book_create')
    else:
        Review.objects.review_creator(book_data, request.session['id'])
    
    return redirect('/books/'+ str(id))

def review_delete(request, id):
    # print "*" * 50
    # print "inside review_delete"
    # print "review_id: " + str(id)
    # print "*" * 50
    review = Review.objects.get(id=id)
    if review.user.id == request.session['id']:
        review.delete()

    return redirect("/books")


