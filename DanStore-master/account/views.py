from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .models import new_form1
from Store_manager.models import *
def registration_final(request):
    return render(request,'account/fianl.html')
def login_view(request):
    if request.user.is_authenticated:
        if hasattr(request.user,'groups'):
                a = request.user.groups.all()[0].name
                if a == 'Company_Admin':
                    return redirect('admin-dashboard')   
                elif a == 'Store_Manager':
                     return redirect('store-dashboard',)
                elif a == 'Dept_Head':
                     return redirect('dept-dashboard',)
                elif a == 'Employe':
                     return redirect('employe_dashboard',)
                elif a == 'Human_Resource':
                     return redirect('hr_dashboard')
        else:
            messages.error(request,'You are not authenticated')
            return render(request, 'Account/login.html')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
           
         
             
            user = authenticate(username=username, password=password)
         
            if hasattr(user,'groups'):
                    a = user.groups.all()[0].name
                    if a == 'Company_Admin':
                        login(request, user)
                        return redirect('admin-dashboard')
                    elif a == 'Store_Manager':
                        login(request, user)
                        return redirect('store-dashboard',)
                    elif a == 'Dept_Head':
                        login(request, user)
                        return redirect('dept-dashboard',)
                    elif a == 'Employe':
                        login(request, user)
                        return redirect('employe_dashboard',)
                    elif a == 'Finance':
                        login(request, user)
                        return redirect('finance_dashboard',)
                    elif a == 'Human_Resource':
                        login(request, user)
                        return redirect('hr_dashboard',)
            else:
                messages.error(request,'Username or password is not correct!')
                return render(request, 'account/login.html')
    return render(request, 'account/login.html')

def registration_form1(request):
    abc=new_form1.objects.all()
    if abc:
        new_form1.objects.all().delete()
        if request.method == "POST":
            First_Name=request.POST.get('firstName')
            Last_Name=request.POST.get('lastname')
            Emila=request.POST.get('email')
            Address=request.POST.get('address')
            phone1=request.POST.get('phone1')
            phone2=request.POST.get('phone2')
            gender=request.POST.get('gender')
            profile_pic=request.FILES.get('img')
            new_form1.objects.create(
                First_Name=First_Name,
                Last_Name=Last_Name,
                Emila=Emila,
                Address=Address,
                phone1=phone1,
                phone2=phone2,
                gender=gender,
                profile_pic=profile_pic)
            return redirect('registration-form2',)
    else:
        if request.method == "POST":
            First_Name=request.POST.get('firstName')
            Last_Name=request.POST.get('lastname')
            Emila=request.POST.get('email')
            Address=request.POST.get('address')
            phone1=request.POST.get('phone1')
            phone2=request.POST.get('phone2')
            gender=request.POST.get('gender')
            profile_pic=request.FILES.get('img')
            from1=new_form1.objects.create(
                First_Name=First_Name,
                Last_Name=Last_Name,
                Emila=Emila,
                Address=Address,
                phone1=phone1,
                phone2=phone2,
                gender=gender,
                profile_pic=profile_pic)
            request.session['id'] = from1.id
            return redirect('registration-form2',)

    return render(request,'account/form1.html',{})

def registration_form2(request):
    a_form1=new_form1.objects.all()[0]
    First_Name=a_form1.First_Name
    Last_Name=a_form1.Last_Name
    Emila=a_form1.Emila
    Address=a_form1.Address
    phone1=a_form1.phone1
    phone2=a_form1.phone2
    gender=a_form1.gender
    profile_pic=a_form1.profile_pic
    b_form2=new_form2.objects.all()
    if b_form2:
        new_form2.objects.all().delete()
        if request.method == "POST":
            Title=request.POST.get('title')
            Filed_Stud=request.POST.get('filed_st')
            Collage=request.POST.get('collage')
            Grade=request.POST.get('grade')
            year=request.POST.get('year')
            file=request.FILES.get('file')
            new_form2.objects.create(
                First_Name=First_Name,
                Last_Name=Last_Name,
                Emila=Emila,
                Address=Address,
                phone1=phone1,
                phone2=phone2,
                gender=gender,
                profile_pic=profile_pic,
                Title=Title,
                Filed_Stud=Filed_Stud,
                Collage=Collage,
                Grade=Grade,
                year=year,
                file=file,
            )
            return redirect('registration-form3',)
    else:
        if request.method == "POST":
            Title=request.POST.get('title')
            Filed_Stud=request.POST.get('filed_st')
            Collage=request.POST.get('collage')
            Grade=request.POST.get('grade')
            year=request.POST.get('year')
            file=request.FILES.get('file')
            new_form2.objects.create(
                First_Name=First_Name,
                Last_Name=Last_Name,
                Emila=Emila,
                Address=Address,
                phone1=phone1,
                phone2=phone2,
                gender=gender,
                profile_pic=profile_pic,
                Titel=Title,
                Filed_Study=Filed_Stud,
                Collage=Collage,
                grade=Grade,
                Year_Graguation=year,
                Document=file,
            )
            return redirect('registration-form3',)

    return render(request,'account/form2.html',{})
def registration_form3(request):
    all_dep=department.objects.all()
    all_store=allStore.objects.all()
    context={
        'all_dep':all_dep,
        'all_store':all_store,
    }
    
    b_form=new_form2.objects.all()[0]
    First_Name=b_form.First_Name
    Last_Name=b_form.Last_Name
    Emila=b_form.Emila
    Address=b_form.Address
    phone1=b_form.phone1
    phone2=b_form.phone2
    gender=b_form.gender
    profile_pic=b_form.profile_pic
    Titel=b_form.Titel
    Filed_Study=b_form.Filed_Study
    Collage=b_form.Collage
    grade=b_form.grade
    Year_Graguation=b_form.Year_Graguation
    Document=b_form.Document
    if request.method == 'POST':
        Branch=request.POST.get('branch')
        Department=request.POST.get('dep')
        role=request.POST.get('role')
        
        unAproved_employees.objects.create(
            First_Name=First_Name,
            Last_Name=Last_Name,
            Emila=Emila,
            Address=Address,
            phone1=phone1,
            phone2=phone2,
            gender=gender,
            profile_pic=profile_pic,
            Titel=Titel,
            Filed_Study=Filed_Study,
            Collage=Collage,
            grade=grade,
            Year_Graguation=Year_Graguation,
            Document=Document,
            Branch=Branch,
            Department=Department,
            role=role,)
        return redirect('thanks')
    return render(request,'account/form3.html',context)
    
    

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    return redirect('login')

