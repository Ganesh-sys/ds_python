from .models import Register,Product,Employee,Registration1
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=('name','passwd','phno','email')


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('pname','pno','pprice','pmanufacture_date','pexepeiry_date')

class  EnquiryForm(forms.Form):
    name=forms.CharField(max_length=30,required=True)
    phno=forms.IntegerField()
    email=forms.EmailField()
    course=forms.CharField(max_length=30,required=True)
    qual=forms.CharField(max_length=20,required=True)
    yop=forms.DateField()

class ContactForm(forms.Form):
    name=forms.CharField(max_length=30,required=True)
    email=forms.CharField(required=True)
    phno=forms.IntegerField()
    course=forms.CharField(max_length=20,required=True)
    comments=forms.CharField(widget=forms.Textarea())

class Reg1form(forms.ModelForm):
    class Meta:
        model=Registration1
        #passwd=forms.CharField(widget=forms.passwordinput())
        fields=('name','passwd','phno','email')

from .models import Post2,Hotel

class PostForm(forms.ModelForm):
    class Meta:
        model=Post2
        fields=('author','title','text','created_date','published_date')


class Hotelform(forms.ModelForm):
    class Meta:
        model=Hotel
        fields=('cname','phno','email','booking_Date','releaving_Date')

class Rest(forms.Form):
    name=forms.CharField(max_length=20,required=True)
    phno=forms.IntegerField()
    email=forms.EmailField()
    course=forms.CharField(max_length=20)
    comments=forms.CharField(widget=forms.Textarea())
    



