from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from .models import User,Book,BookCategory,Cart,Order
from django.urls import resolve
from django.http import HttpRequest
from django.utils import timezone

not_found = False
# Create your views here.
current_url = ''
def index(request):
	global not_found
	all_book = Book.objects.all()
	global current_url
	current_url = request.path
	if request.method == 'POST':
		form_login = LoginForm(request.POST)
		if form_login.is_valid():
			u_name = request.POST['user_name']
			password = request.POST['password']
			temp_user = User.objects.filter(user_name = u_name,password = password)
			try:
				t_user = User.objects.get(user_name=u_name,password=password)
			except:
				pass


			if len(temp_user) > 0:
				print('login done')
				request.session['username'] = u_name
				request.session['u_id'] = t_user.id

				not_found = False
				#return redirect('/')
			else:

				not_found = True
				#return redirect('/')
			try:
				if request.session.get('username'):
					isset = True
					user = request.session['username']
				else:
					isset = False
					user = ''
			except:
				pass
		context = {'form':form_login,'isset':isset,'user':user,'all_book':all_book,'not_found':not_found}
		return render(request,'home/index.html',context)



	else:
		not_found = False
		form_login = LoginForm()
		try:
			if request.session.get('username'):
				isset = True
				user = request.session['username']
			else:
				isset = False
				user = ''
		except:
			pass

		context = {'form':form_login,'isset':isset,'user':user,'all_book':all_book,'not_found':not_found}
		return render(request,'home/index.html',context)


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = User(user_name=request.POST['user_name'],email_id=request.POST['email_id'],password=request.POST['password'],name=request.POST['name'],shipping_addr=request.POST['shipping_addr'],phone_no=request.POST['phone_no'])
			new_user.save()
			return redirect('/')
	else:
		form = RegisterForm()


	context = {'form':form}

	return render(request,'home/register.html',context)


def logout(request):
	if request.method == 'POST':
		try:
			del request.session['username']
			del request.session['u_id']



		except:
			pass
	print(request.path)
	return redirect(current_url)



def books(request,booktype):
	global current_url
	current_url = request.path
	temp_book = Book.objects.filter(book_category=booktype)
	book_c = BookCategory.objects.get(pk=booktype)
	try:
			if request.session.get('username'):
				user = request.session['username']
				isset = True
			else:
				user = ''
				isset = False
	except:
			pass
	context = {'show_book':temp_book,'user':user,'book_c':book_c,'isset':isset}
	return render(request,'home/books.html',context)



def add(request,bookid):
	subject = Book.objects.get(pk=bookid)
	temp_add = Cart(order_item = bookid,user_id=request.session['u_id'])
	temp_add.save()
	return redirect('/books/{}'.format(subject.book_category))




def cart(request):
	global current_url
	current_url = '/'
	cart_list = []
	total = 0
	book_ref = Cart.objects.filter(user_id = request.session['u_id'])
	for book_id in book_ref:

		ref_dic = {}
		t = Book.objects.get(pk=book_id.order_item)
		total = total + t.book_price
		ref_dic['un_book_id'] = t.pk
		ref_dic['book_name'] = t.book_name
		ref_dic['book_price'] = t.book_price
		ref_dic['book_image'] = t.book_image
		ref_dic['book_author'] = t.author_name
		cart_list.append(ref_dic)
	print(book_ref)


	try:
			if request.session.get('username'):
				user = request.session['username']
				isset = True
			else:
				user = ''
				isset = False
	except:
			pass
	amt = total + 50
	len_cart = len(cart_list)
	context = {'user':user,'isset':isset,'cart_list':cart_list,'total':total,'amt':amt,'len_cart':len_cart}
	return render(request,'home/cart.html',context)


def remove(request,un_book_id):
	login_user = request.session['u_id']
	book_remove_id = un_book_id
	Cart.objects.filter(user_id=login_user,order_item=book_remove_id).delete()
	return redirect('/cart')


def confirmation(request):
	if request.method == 'POST':
		global current_url
		current_url = '/'
		order_list = []
		active_user = request.session['u_id']
		order_books = Cart.objects.filter(user_id=active_user)
		for b in order_books:
			order_list.append(b.order_item)
		final_str = str(order_list)
		order_confirm_add = Order(delivery_user_id=active_user,date_placed=timezone.localtime(timezone.now()),order_items=final_str)
		order_confirm_add.save()

		user_info = User.objects.get(pk=active_user)
		# order_p_id = Order.objects.get(date_placed=time_of_order).pk
		order_item_names = []
		order_item_price = []
		for oi in order_list:
			product_name = Book.objects.get(pk=oi)
			order_item_names.append(product_name.book_name)
			order_item_price.append(product_name.book_price)
		date_of_order = timezone.localtime(timezone.now())
		date_of_delivery = date_of_order + timezone.timedelta(days=7)
		sub = 0
		for x in order_item_price:
			sub = sub + x
        #------------------------------------------------------------------
		try:
			if request.session.get('username'):
				user = request.session['username']
				isset = True
			else:
				user = ''
				isset = False
		except:
			pass
		context = {'user':user,'isset':isset,'user_info':user_info,'order_item_names':order_item_names,'date':date_of_order,'sum':sub,'d_date':date_of_delivery}
		return render(request,'home/confirmation.html',context)
