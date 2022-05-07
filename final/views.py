import email
from multiprocessing import context
from .models import Faqs, User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView  
from .models import Post
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from final.forms import CreateUserForm 
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
# making function for home page
def home(request):
    total_tax = 0 #defining variable for tax amount deduction amount and total income
    total_deduction=0
    total_salary = 0
    if request.method == 'POST' and 'calculate' in request.POST:
        sal = request.POST['salary']
        bon = request.POST['Bonus']
        allo = request.POST['allowance']
        oth = request.POST['others']
        
        fund1 = request.POST['Fund']
        dons = request.POST['donation']
        trust = request.POST['trust']
        medi = request.POST['medical']
        ins = request.POST['insurance']
        others_2 = request.POST['other']
        
        try: #using try block for exception handling
            salary = int(float(sal))
            bonus = int(bon)
            allow = int(allo)
            other = int(oth)
            funds = int(fund1)
            donation = int(dons)
            trusts = int(trust)
            medical = int(medi)
            insurance = int(ins)
            others = int(others_2)
            total_deduction = funds + donation+ trusts+ medical + insurance+ others
            print("total_deduction",total_deduction)

            total_income = salary + bonus + allow + other
            print("total_income",total_income)
            total_salary = total_income - total_deduction
            
            print("salary",salary)
            print("allowance",allow)
            print("bonus",bonus)
            print("other",other)
            print("total_income",total_income)
            print("providen fund",funds)
            print("donation",donation)
            print("Citizen investment trust",trusts)
            print("medical expenses",medical)
            print("insurance",insurance)
            print("others",others)

            

            if total_salary <=400000:
                total_tax= total_tax+total_salary*(0.01)
                print("total_tax",total_tax)
            elif total_salary > 400000 and total_salary <=500000:
                total_tax = total_tax+total_salary*(0.1)
                print("total_tax",total_tax)
            elif total_salary > 500000 and total_salary <=700000:
                total_tax = total_tax+total_salary*(0.2)
                print("total_tax",total_tax)
            elif total_salary > 700000 and total_salary <=2000000:
                total_tax = total_tax+total_salary*(0.3)
                print("total_tax",total_tax)
            else:
                total_tax= total_tax+total_salary*(0.36)
                print("total_tax",total_tax)
        except:
            print('Cannot convert string to int')
       
    return render(request, 'index.html',{'tax_amount':total_tax,'deduction_amount':total_deduction,'income_amount':total_salary})

class BlogListView(ListView): #making class for news page
    model = Post
    template_name = 'news.html'

class BlogDetailView(DetailView): #making class for individual news page
    model = Post
    template_name = 'inside-news.html'

def faqs(request):  # making function for faqs page
    context={
        'faqs' : Faqs.objects.all()
    }
    return render(request,'faqs.html', context)
def aboutus(request):  # making function for aboutus page
    return render(request,'aboutus.html')  

def signup(request):
    
    if request.method=="POST":
        usernam= request.POST['username']
        fname= request.POST['first_name']
        lname= request.POST['last_name']
        email= request.POST['email']
        pass1= request.POST['password1']
        pass2= request.POST['password2']

        
        # if User.objects.filter(email=email):
        #     messages.error(request,'Email already exist')
           
   
        if User.objects.filter(username=usernam):
            messages.error(request,'Username already exist')
            return redirect(signup)
        if pass1!=pass2:
            messages.error(request,"Password Didin't match.")
            return redirect(signup)
            

        myuser=User.objects.create_user(usernam,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        
        messages.success(request, 'Your account was created successfully' )
        return redirect('signin')
       
    return render(request, 'signup.html')
    

def signin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username Or Password Is Incorrect')


    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect("signin")

def profileuser(request):
   return render(request,"profile.html")

# def viewuser(request):
#     context={
#         'user': request.user
#     }
#     return render(request, 'profile.html', context)


def viewHistory(request):
   return render(request,"history.html")


def vat(request):
    total_tax=0
    total_price=0
    totall=0
    
    if request.method == 'POST' and 'calculate' in request.POST:
        sal = request.POST['price']
        tax = request.POST['vatax']


        try: #using try block for exception handling
            sala = int(float(sal))
            totaltax = int(float(tax))/100
            totall= sala
            print("salary",totall)

            total_tax=sala * totaltax
            print("totaltax",total_tax)

            total_price=sala+total_tax
            print("price",total_price)




            


        except:
            print('Cannot convert string to int')
            
    return render(request, 'vat.html',{'tax_amount':total_tax,'deduction_amount':total_price,'income_amount':totall})

