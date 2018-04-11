from django.shortcuts import render,redirect
from django.urls import resolve
from django.http import HttpRequest
from django.utils import timezone
from home.models import Book
from .models import Admin
from .forms import BookAdd,AdminLogin

# Create your views here.
def admin(request):
	if request.method == 'POST':
		form = BookAdd(request.POST,request.FILES)
		if form.is_valid():
			new_book = Book(book_name=request.POST['book_name'],author_name=request.POST['author_name'],book_category=request.POST['book_category'],book_description=request.POST['book_description'],book_price=request.POST['book_price'],book_image=request.FILES['book_image'])
			new_book.save()
			
	else:
		form = BookAdd()
     

	context = {'form':form,'admin_name':request.session['admin_name']}
	return render(request,'adminlogin/index.html',context)


def login(request):
	if request.session.get('admin_name'):
		return redirect('add/')
	else:
		if request.method == 'POST':
			form = AdminLogin(request.POST)
			if form.is_valid():
				temp = Admin.objects.filter(admin_name=request.POST['admin_name'],admin_password=request.POST['admin_password'])
				if len(temp)==1:
					request.session['admin_name'] = request.POST['admin_name']
					return redirect('add/')
				else:
					print('Invaid Credentials')

			
		else:
			form = AdminLogin()
		print(request.path)
		context = {'form':form}
		return render(request,'adminlogin/login.html',context)


def logout(request):
	if request.method == 'POST':
		del request.session['admin_name']
	return redirect('/adminlogin/')


	