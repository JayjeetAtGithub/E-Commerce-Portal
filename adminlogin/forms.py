from django import forms
CHOICES = (
('1','Mathematics'),
('2','Physics'),
('3','Chemistry'),
('4','Computer Sc.')
)
class BookAdd(forms.Form):
	book_name = forms.CharField(label='Book Name',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the name of the book'}))
	author_name = forms.CharField(label='Authors Name',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Authors name'}))
	book_description = forms.CharField(label='Book Description',max_length=255,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter book description'}))
	book_image = forms.ImageField(widget=forms.FileInput())
	book_price = forms.IntegerField(label='Book Price',widget=forms.NumberInput(attrs={'min':'0','max':'10000','step':'1','class':'form-control','placeholder':'Price of book'}))
	book_category = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=CHOICES)

class AdminLogin(forms.Form):
	admin_name = forms.CharField(label='Username',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','style':'width:40%;margin:auto;'}))
	admin_password = forms.CharField(label='Password',max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','style':'width:40%;margin:auto;'}))
