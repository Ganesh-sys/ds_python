from django.shortcuts import render
from django.http import HttpResponse
#from django.http import HttpResponseRedirect

def TestHome(request):
    return HttpResponse('<h1>welcome to my testapp</h1>')


def Power(request):
    return HttpResponse(" welcome to power star pawan kalyan")

# Create your views here.
from .models import Student

def DisplayCoursesInfo(request):
    context={'coursedb':Student.objects.all()}
    return render(request,'coursesdb.html',context)


from .forms import RegisterForm
from .models import Register
from django.http import HttpResponseRedirect
def RegisterView(request):
    form_class=RegisterForm
    context={'form':form_class}
    if request.method=="POST":
        form=RegisterForm(request.POST)

        if form.is_valid():
            vname=form.cleaned_data['name']
            vpasswd=form.cleaned_data['passwd']
            vphno=form.cleaned_data['phno']
            vemail=form.cleaned_data['email']
            Register.objects.create(name=vname,passwd=vpasswd,phno=vphno,email=vemail)
            return HttpResponseRedirect('Power')

    return render(request,'registerform.html',context)

def college(request):
    return HttpResponse("<h1>Thanks for visiting</h1>")


from .models import Post1

def BlogPost(request):
    context={'blogdb':Post1.objects.all()}
    return render(request,'blogdata.html',context)


from .models import Product
from .forms import ProductForm

def Productview(request):
    #context={'blog':Product.objects.all()}
    if request.method=="POST":
        form=ProductForm(request.POST)

        if form.is_valid():
            pname=form.cleaned_data['pname']
            pno=form.cleaned_data['pno']
            pprice=form.cleaned_data['pprice']
            pmanufacture_date=form.cleaned_data['pmanufacture_date']
            pexepeiry_date=form.cleaned_data['pexepeiry_date']

            Product.objects.create(pname=pname,pno=pno,pprice=pprice,pmanufacture_date=pmanufacture_date,pexepeiry_date=pexepeiry_date)
            return HttpResponseRedirect('col')

        else:
            context = {'form':form}
            return render(request,'blog1.html',context)



    else:
        form=ProductForm
        context={'form':form}

        return render(request,'blog1.html',context)

from .forms import EnquiryForm
from .models import Employee

def EnqiryView(request):
    print(request.method)
    form_class=EnquiryForm
    context={'form':form_class}
    if request.method=="POST":
        form=EnquiryForm(request.POST)
        vname=request.POST['name']
        vphno=request.POST['phno']
        vemail=request.POST['email']
        vcourse=request.POST['course']
        vqual=request.POST['qual']
        vyop=request.POST['yop']
        print("Name:",vname)
        print("phno:",vphno)
        print("email:",vemail)
        print("course:",vcourse)
        print("qual:",vqual)
        print("yop:",vyop)

    return render(request,'EnquiryForm.html',context)


def Thanks(request):
    return HttpResponse("Thanks for contacting us and you will have a message from us")

from .forms import ContactForm
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect

def Contact(request):
    form_class=ContactForm
    context={'form':form_class} 

    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            contact_name=form.cleaned_data['name']
            contact_email=form.cleaned_data['email']
            phno=form.cleaned_data['phno']
            course=form.cleaned_data['course']
            comments=form.cleaned_data['comments']
            subject="A new contact or lead- {}".format(contact_name)
            email=EmailMessage(subject,contact_name + '\n' + contact_email + '\n' + str(phno) +'\n'+course+'\n'+comments,to=['ganeshchowdary052@gmail.com'])
            email.send()
            return HttpResponseRedirect('/testapp5/thank')


    return render(request,'contact_blog.html',context)


from .forms import Reg1form
from .models import Registration1
from django.http  import HttpResponseRedirect

def Regview(request):
    form_class=Reg1form
    context={'form':form_class}

    if request.method == 'POST':
        form=Reg1form(request.POST)
        if form.is_valid():
            vname=form.cleaned_data['name']
            vpasswd=form.cleaned_data['passwd']
            vphno=form.cleaned_data['phno']
            vemail=form.cleaned_data['email']
            Registration1.objects.create(name=vname,passwd=vpasswd,phno=vphno,email=vemail)

        return HttpResponseRedirect('/testapp5/thank')

    return render(request,'contact_blog1.html',context)



from .models import Post2,Hotel
from django.http  import HttpResponseRedirect

def Blog(request):
    context={'blog':Post2.objects.all()}
    return render(request,'loaddata.html',context)

from .forms import PostForm,Hotelform
def blogview(request):
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            author=form.cleaned_data['author']
            title=form.cleaned_data['title']
            text=form.cleaned_data['text']
            created_date=form.cleaned_data['created_date']
            published_date=form.cleaned_data['published_date']

            Post2.objects.create(author=author,title=title,text=text,created_date=created_date,published_date=published_date)
        return HttpResponseRedirect('/testapp5/col')
        #else:
            #context={'form':form}
            #return render(request,'blog_form.html',context)
    else:
        form=PostForm
        context={'form':form}
        return render(request,'blog_form.html',context)

from .models import Hotel
def Hotelview(request):
    context={'cont':Hotel.objects.all()}
    return render(request,'load1.html',context)

def hotelview(request):
    if request.method == 'POST':
        form=Hotelform(request.POST)
        if form.is_valid():
            cname=form.cleaned_data['cname']
            phno=form.cleaned_data['phno']
            email=form.cleaned_data['email']
            booking_Date=form.cleaned_data['booking_Date']
            releaving_Date=form.cleaned_data['releaving_Date']

            Hotel.objects.create(cname=cname,phno=phno,email=email,booking_Date=booking_Date,releaving_Date=releaving_Date)
        return HttpResponseRedirect('/testapp5/col')
    else:
        form=Hotelform
        context={'form':form}
        return render(request,'blog_form2.html',context)
#from .models import Hotel

#def Loadblog(request):
    #context={'blog1':Hotel.objects.all()}
    #return render(request,'/testapp5/logdata.html',context)

def Ref(request):
    return HttpResponse("<h1> Thank you and have a great day")

from .forms import Rest
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect

def contact1(request):
    #get request
    form_class=Rest
    context={'form':form_class}

    #post request
    if request.method=="POST":
        form=Rest(request.POST)

        if form.is_valid():
            c_name=form.cleaned_data['name']
            c_phno=form.cleaned_data['phno']
            c_email=form.cleaned_data['email']
            c_course=form.cleaned_data['course']
            c_comments=form.cleaned_data['comments']

            subject="A new contact or lead-{}".format(c_name)
            email=EmailMessage(subject,c_name+'\n'+str(c_phno)+'\n'+c_email+'\n'+c_course+'\n'+c_comments, to=['ganeshn2109@gmail.com','ganeshchowdary052@gmail.com'])
            email.send()
            return HttpResponseRedirect('/testapp5/sinfo')
    return render(request,'contact_blog.html',context)













