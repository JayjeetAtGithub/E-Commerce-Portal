from django.db import models
from django.utils import timezone

# Create your models here.
class BookCategory(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Book(models.Model):
	book_category = models.IntegerField()
	book_name = models.CharField(max_length=500)
	author_name = models.CharField(max_length=500)
	book_description = models.TextField(max_length=500)
	book_image = models.FileField(null=True,blank=True)
	book_price = models.IntegerField()

	def __str__(self):
		return self.book_name


class User(models.Model):
	user_name = models.CharField(max_length=255)
	email_id = models.EmailField(max_length=255)
	password = models.CharField(max_length=255)
	name = models.CharField(max_length=255,default='')
	shipping_addr = models.CharField(max_length=255,default='')
	phone_no = models.CharField(max_length=255,default='')

	def __str__(self):
		return self.user_name + self.email_id + self.password



class Cart(models.Model):
	user_id = models.IntegerField()
	order_item = models.IntegerField()


class Order(models.Model):
	delivery_user_id = models.IntegerField()
	date_placed = models.DateTimeField()
	order_items = models.CharField(max_length=255)
