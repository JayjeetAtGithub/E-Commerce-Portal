from django import forms

class RegisterForm(forms.Form):
	user_name = forms.CharField(label='Username',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Choose a suitable username'}))
	email_id = forms.EmailField(label='EmailID',max_length=100,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email-id'}))
	password = forms.CharField(label='Password',max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Choosea a suitable password'}))
	name = forms.CharField(label='name',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}))
	shipping_addr = forms.CharField(label='shipping_addr',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
	phone_no = forms.CharField(label='phone_no',max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Contact Number'}))



class LoginForm(forms.Form):
	user_name = forms.CharField(label='Username',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	password = forms.CharField(label='Password',max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
