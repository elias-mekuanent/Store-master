from django.shortcuts import render,redirect
from Store_manager.models import *
from django.db.models import Q
from django.contrib.auth.models import User, Group
from django.contrib import messages
from Store_manager.models import *
from account.models import *
from django.core.mail import send_mail
import random
import string
from random_username.generate import generate_username
from .form import *
from django.contrib.auth import update_session_auth_hash

def hr_dashboard(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            totall_NoEmp=employ.objects.all().count()
            totall_NoDep=department.objects.all().count()
            totall_NoRole=allRole.objects.all().count()
            allEmployees = employ.objects.all()
            allunAprove=unAproved_employees.objects.filter(cheek=None).count()
            context={
                'totall_NoEmp':totall_NoEmp,
                'totall_NoDep':totall_NoDep,
                'totall_NoRole':totall_NoRole,
                'allEmployees':allEmployees,
                'allunAprove':allunAprove,
                'admin':admin,
            }
        
            return render(request,'human_resource/index.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
 
#----------------- MANAGE EMPLOYEE ---------------#
def manage_employee(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            allEmployees = employ.objects.all()
            context = {
                'all_emplyees': allEmployees,
                'admin':admin,
            }

            return render(request,'human_resource/ManageEmployee/index.html', context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
   


def add_new_employe(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
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
                    new = User.objects.filter(email=Emila)
                    if new.count():
                            messages.error(request, "Eamil Already Exist")
                            return redirect('hr-add-new-employe')
                    else:
                        new_form1.objects.create(
                            First_Name=First_Name,
                            Last_Name=Last_Name,
                            Emila=Emila,
                            Address=Address,
                            phone1=phone1,
                            phone2=phone2,
                            gender=gender,)
                        return redirect('hr_registration-form2',)
            else:
                if request.method == "POST":
                    First_Name=request.POST.get('firstName')
                    Last_Name=request.POST.get('lastname')
                    Emila=request.POST.get('email')
                    Address=request.POST.get('address')
                    phone1=request.POST.get('phone1')
                    phone2=request.POST.get('phone2')
                    gender=request.POST.get('gender')
                    new = User.objects.filter(email=Emila)
                    if new.count():
                            messages.error(request, "Eamil Already Exist")
                            return redirect('hr-add-new-employe')
                    else:
                        from1=new_form1.objects.create(
                            First_Name=First_Name,
                            Last_Name=Last_Name,
                            Emila=Emila,
                            Address=Address,
                            phone1=phone1,
                            phone2=phone2,
                            gender=gender,
                            )
                    
                        return redirect('hr_registration-form2',)
            return render(request,'human_resource/ManageEmployee/add_new_employee.html',{})
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
  

def hr_registration_form2(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':

            a_form1=new_form1.objects.all()[0]
            First_Name=a_form1.First_Name
            Last_Name=a_form1.Last_Name
            Emila=a_form1.Emila
            Address=a_form1.Address
            phone1=a_form1.phone1
            phone2=a_form1.phone2
            gender=a_form1.gender
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
                        Title=Title,
                        Filed_Stud=Filed_Stud,
                        Collage=Collage,
                        Grade=Grade,
                        year=year,
                        file=file,
                    )
                    return redirect('hr_registration-form3',)
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
                        Titel=Title,
                        Filed_Study=Filed_Stud,
                        Collage=Collage,
                        grade=Grade,
                        Year_Graguation=year,
                        Document=file,
                    )
                    return redirect('hr_registration-form3',)
            return render(request,'human_resource/ManageEmployee/add_new_employee_form2.html',{})
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def hr_registration_form3(request):
    username= generate_username(1)[0]
    length=8
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    password=result_str
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
    Full_Name=First_Name + Last_Name
    if request.method == 'POST':
        Branch=request.POST.get('branch')
        Department=request.POST.get('dep')
        role=request.POST.get('role')
        new = User.objects.filter(username=username)
        access_store=allStore.objects.get(storeName=Branch)
        if new.count():
            messages.error(request, "User Already Exist")
            print("User Already Exist")
            return redirect('hr_registration-form3')
        else:
            user = User.objects.create_user(
                        username=username, 
                        email=Emila, 
                        password=password, 
                        first_name=First_Name, 
                        last_name=Last_Name)
            user.save()
        if  role == 'Employe':
                    new_group = Group.objects.get(name='Employe')
                    new_group.user_set.add(user)
                    newEmployee = employ.objects.create(user=user,
                    role=role,
                    Full_Name=Full_Name,
                    gender=gender,
                    accessStore=access_store,
                    address=Address,
                    phone1=phone1,
                    phone2=phone2,
                    Titel=Titel,
                    Filed_Study=Filed_Study,
                    profile_pic=profile_pic,
                    Collage=Collage,
                    grade=grade,
                    Year_Graguation=Year_Graguation,
                    Document=Document,
                    inDepartment=Department
                    )
                    if newEmployee:
                        send_mail(
                                    ' Wellcome DanEnergy ',
                                    'Dear '+ First_Name + '\n' + 'This is your username and password \n'+ 'Username: ' +  username + '\n' + 'Password: ' +  password + '\n' + 'Please change your username and password before proceeding.',
                                    'bgiethipia.hade@gmail.com',
                                    [Emila],
                                    fail_silently=False,)
                        
                        messages.success(request,'You Have Successfully Created New Employee')
                        
                        return redirect('hr-manage-employee')
    return render(request,'human_resource/ManageEmployee/add_new_employee_form3.html',context)


def employe_ditel(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            req_emp=employ.objects.get(pk=id)
            all_dep=department.objects.all()
            context={
                'req_emp':req_emp,
                'all_dep':all_dep,
                'admin':admin,
            }
            return render(request,'human_resource/ManageEmployee/employe_ditel.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def aprove_employe(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            allUnAprove=unAproved_employees.objects.filter(cheek=None)
            context={
                'allUnAprove':allUnAprove,
                'admin':admin,
            }
            return render(request,'human_resource/ManageEmployee/aprove_employe.html',context)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def unapproveEmploye_ditel(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            un_employ=unAproved_employees.objects.get(pk=id)
            context={
                'un_employ':un_employ,
                'admin':admin,
            }
            return render(request,'human_resource/ManageEmployee/unapproved_detial.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def rejected_emp_approved_request(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            allUnAprove=unAproved_employees.objects.filter(cheek=False)
            context={
                'allUnAprove':allUnAprove,
                'admin':admin,
            }
            return render(request,'human_resource/ManageEmployee/rejected_applicant.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def reject_request(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            un_employ=unAproved_employees.objects.get(pk=id)
            un_employ.cheek=False
            un_employ.save()
            return redirect('rejected-emp-approved-request')
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def approve_unaproved_emp(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':

            username= generate_username(1)[0]
            length=8
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(length))
            password=result_str
            un_employ=unAproved_employees.objects.get(pk=id)
            un_employ.cheek = True
            un_employ.save()
            email=un_employ.Emila
            firstName=un_employ.First_Name
            lastName=un_employ.Last_Name
            role=un_employ.role
            gender=un_employ.gender
            access_store1=un_employ.Branch
            access_store=allStore.objects.get(storeName=access_store1)
            Full_Name=firstName + lastName
            address=un_employ.Address
            phone1=un_employ.phone1
            phone2=un_employ.phone2
            profile_pic=un_employ.profile_pic
            Titel=un_employ.Titel
            Filed_Study=un_employ.Filed_Study
            Collage=un_employ.Collage
            grade=un_employ.grade
            Year_Graguation=un_employ.Year_Graguation
            Document=un_employ.Document
            inDepartment=un_employ.Department
            
            new = User.objects.filter(username=username)
            if new.count():
                messages.error(request, "User Already Exist")
            else:
                new = User.objects.filter(email=email)
                if new.count():
                        messages.error(request, "Eamil Already Exist")
                else:
                    user = User.objects.create_user(
                                username=username, 
                                email=email, 
                                password=password, 
                                first_name=firstName, 
                                last_name=lastName)
                    user.save()
                
                    if user:
                        if  role == 'Employe':
                            new_group = Group.objects.get(name='Employe')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,
                            role=role,
                            Full_Name=Full_Name,
                            gender=gender,
                            accessStore=access_store,
                            address=address,
                            phone1=phone1,
                            phone2=phone2,
                            Titel=Titel,
                            Filed_Study=Filed_Study,
                            profile_pic=profile_pic,
                            Collage=Collage,
                            grade=grade,
                            Year_Graguation=Year_Graguation,
                            Document=Document,
                            inDepartment=inDepartment
                            )
                            if newEmployee:
                                send_mail(
                                            ' Wellcome DanEnergy ',
                                            'Dear '+ firstName + '\n' + 'This is your username and password \n'+ 'Username: ' +  username + '\n' + 'Password: ' +  password + '\n' + 'Please change your username and password before proceeding.',
                                            'bgiethipia.hade@gmail.com',
                                            [email],
                                            fail_silently=False,)
                                
                                messages.success(request,'You Have Successfully Created New Employee')
                                
                                return redirect('hr-manage-employee')
                        elif (role == 'Dept_Head'):
                            new_group = Group.objects.get(name='Dept_Head')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,
                            role=role,
                            Full_Name=Full_Name,
                            gender=gender,
                            accessStore=access_store,
                            address=address,
                            phone1=phone1,
                            phone2=phone2,
                            Titel=Titel,
                            Filed_Study=Filed_Study,
                            profile_pic=profile_pic,
                            Collage=Collage,
                            grade=grade,
                            Year_Graguation=Year_Graguation,
                            Document=Document,
                            inDepartment=inDepartment
                            )
                            if newEmployee:
                                send_mail(
                                            ' Wellcome DanEnergy ',
                                            'Dear '+ firstName + '\n' + 'This is your username and password \n'+ 'Username: ' +  username + '\n' + 'Password: ' +  password + '\n' + 'Please change your username and password before proceeding.',
                                            'bgiethipia.hade@gmail.com',
                                            [email],
                                            fail_silently=False,)
                                
                                messages.success(request,'You Have Successfully Created New Employee')
                                
                                return redirect('hr-manage-employee')
                        elif (role == 'Store_Manager'):
                            new_group = Group.objects.get(name='Store_Manager')
                            newEmployee = employ.objects.create(user=user,
                            role=role,
                            Full_Name=Full_Name,
                            gender=gender,
                            accessStore=access_store,
                            address=address,
                            phone1=phone1,
                            phone2=phone2,
                            Titel=Titel,
                            Filed_Study=Filed_Study,
                            profile_pic=profile_pic,
                            Collage=Collage,
                            grade=grade,
                            Year_Graguation=Year_Graguation,
                            Document=Document,
                            inDepartment=inDepartment
                            )
                            if newEmployee:
                                send_mail(
                                            ' Wellcome DanEnergy ',
                                            'Dear '+ firstName + '\n' + 'This is your username and password \n'+ 'Username: ' +  username + '\n' + 'Password: ' +  password + '\n' + 'Please change your username and password before proceeding.',
                                            'bgiethipia.hade@gmail.com',
                                            [email],
                                            fail_silently=False,)
                                
                                messages.success(request,'You Have Successfully Created New Employee')
                                return redirect('hr-manage-employee')
                    elif(role == 'Finance'):
                        new_group = Group.objects.get(name='Finance')
                        new_group.user_set.add(user)
                        newEmployee = employ.objects.create(user=user,
                            role=role,
                            Full_Name=Full_Name,
                            gender=gender,
                            accessStore=access_store,
                            address=address,
                            phone1=phone1,
                            phone2=phone2,
                            Titel=Titel,
                            Filed_Study=Filed_Study,
                            profile_pic=profile_pic,
                            Collage=Collage,
                            grade=grade,
                            Year_Graguation=Year_Graguation,
                            Document=Document,
                            inDepartment=inDepartment
                            )
                        if newEmployee:
                            send_mail(
                                        ' Wellcome DanEnergy ',
                                        'Dear '+ firstName + '\n' + 'This is your username and password \n'+ 'Username: ' +  username + '\n' + 'Password: ' +  password + '\n' + 'Please change your username and password before proceeding.',
                                        'bgiethipia.hade@gmail.com',
                                        [email],
                                        fail_silently=False,)
                            
                            messages.success(request,'You Have Successfully Created New Employee')
                            return redirect('hr-manage-employee')
            return redirect('hr-aprove-employe')



        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
    
#----------------- END of manage Employee ---------------#

def hr_department(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
                users = User.objects.get(id=request.user.id)
                re_employ=employ.objects.get(user=users)
                admin = re_employ
                all_depts = department.objects.all()
                dep_emp={}
                all_dep_name=[]
                num=[]
                for dep in all_depts:
                        all_dep_name.append(dep.departmentName)
                
                for dep in all_dep_name:
                    dep_emp[dep]=employ.objects.filter(inDepartment=dep).count()
                for i,j in dep_emp.items():
                    num.append(j)
                data=zip(all_depts, num)
                print(dep_emp)
                context={
                    'all_dept': all_depts,
                    'data':data,
                    'admin':admin,
                }
                return render(request,'human_resource/Departments/index.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def hr_department_detail(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            DeptHead = employ.objects.filter(role = 'Dept_Head')
            req_dep=department.objects.get(pk=id)
            all_emp=employ.objects.filter(role='Employe')
            indep=req_dep.departmentName
            all_employer=employ.objects.filter(inDepartment=indep)
            context={
                "departmentHeads" : DeptHead,
                'selectedDepartment':req_dep,
                'all_emp':all_emp,
                'all_employer':all_employer,
                'admin':admin,
            }
            return render (request,'human_resource/Departments/department_details.html',context)


   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def add_emp_to_dep(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            if request.method == 'POST':
                    full_name=request.POST.get('employe')
                    dep_name=request.POST.get('departmentName')
                    print(full_name)
                    print(dep_name)
                    selec_dep=department.objects.get(departmentName=dep_name)
                    dep=selec_dep.departmentName
                    select_emp=employ.objects.get(Full_Name=full_name)
                    select_emp.inDepartment=dep
                    select_emp.save()
                    return redirect('hr-department-detail',selec_dep.id)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def hr_set_dept_head(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
           if request.method =="POST":
                dept_id=request.POST.get('departmentId')
                dept_head=request.POST.get('dept_head')
                update_dept=department.objects.get(id=dept_id)
                update_dept.departmentHead = dept_head
                update_dept.save()
                print("dept_id",dept_id)
                print("dept_head",dept_head)
                return redirect('hr-department-detail',dept_id)

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def hr_dept_name_change(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            if request.method =="POST":
                    dept_id=request.POST.get('departmentId')
                    dept_name=request.POST.get('deptname')
                    update_dept=department.objects.get(id=dept_id)
                    update_dept.departmentName = dept_name
                    update_dept.save()
                    print("dept_id",dept_id)
                    print("dept_head",dept_name)
                    return redirect('hr-department-detail',dept_id)
            
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def hr_department_delete(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            department.objects.get(id=id).delete()
            return redirect('hr-department')

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def hr_add_new_department(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            context={
            'admin':admin,
            }
            if request.method == 'POST':
                departmentName = request.POST.get('departmentName')
                departmentDescription = request.POST.get('departmentDescription')
                all_dep=department.objects.filter(departmentName=departmentName)
            if all_dep.count():
                messages.error(request, "Department Name Already Exist")
                return render(request,'human_resource/Departments/add_new_department.html',context)
            else:
                dept = department.objects.create(departmentName = departmentName,departmentDescription=departmentDescription)
                if dept:
                    messages.success(request,'You Have Successfully added new department.')
                    return redirect('hr-department')
            return render(request,'human_resource/Departments/add_new_department.html',context)
    
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def manage_emp_role(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            req_emp=employ.objects.get(pk=id)
            user=req_emp.user
            if request.method == 'POST':
                if request.POST.get('r1') == 'on':
                    req_emp.role = 'Employe'
                    user.groups.clear()
                    new_group = Group.objects.get(name='Employe')
                    new_group.user_set.add(user)
                elif request.POST.get('r2') == 'on':
                    req_emp.role = 'Dept_Head'
                    user.groups.clear()
                    new_group = Group.objects.get(name='Dept_Head')
                    new_group.user_set.add(user)
                elif request.POST.get('r3') == 'on':
                    req_emp.role = 'Store_Manager'
                    user.groups.clear()
                    new_group = Group.objects.get(name='Store_Manager')
                    new_group.user_set.add(user)
                elif request.POST.get('r4') == 'on':
                    req_emp.role = 'Finance'
                    user.groups.clear()
                    new_group = Group.objects.get(name='Finance')
                    new_group.user_set.add(user)
                new=request.POST.get('R1')
                print('this is:',new)
                req_emp.save()
            return redirect('employe-ditel',id)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def hr_set_dept_emp(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
                req_emp=employ.objects.get(pk=id)
                
                if request.method == 'POST':
                    dept_name=request.POST.get('dept_name')
                    print(dept_name)
                    req_emp.inDepartment=dept_name
                req_emp.save()  
                return redirect('employe-ditel',id)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  
    
def hr_active_status(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            req_emp=employ.objects.get(pk=id)
            print(req_emp.user.is_active)
            if request.method == 'POST':
                if (request.POST.get('active')) == 'on':
                    req_emp.user.is_active = True
                else:
                    req_emp.user.is_active = False
                
            req_emp.user.save() 
            return redirect('employe-ditel',id)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
    
def role_details(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            user=User.objects.get(id=request.user.id)
            group=Group.objects.get(user=user)

            context={
                'req_emp':group,
                'user':user,
                'admin':admin,
            }
            return render(request,'human_resource/role_details.html',context)


   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

# ------------------------ Chat ----------------------------------------------

def hr_chat(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            me_with=exploreU
            my_message=chatbot.objects.filter(me_with=me_with)
            admin = exploreU
            me=exploreU.user
            me_with=exploreU
            all_chate_team=[]
            all_chat=chatbot.objects.filter(Q(me_with=me_with) | Q(me=me))
            for a in all_chat:
                if a.me_with in all_chate_team:
                    pass
                else:
                    all_chate_team.append(a.me_with)
            if request.method == 'POST':
                user=request.POST.get('serach')
                serch=User.objects.get(username=user)
                chat_group1=employ.objects.get(user=serch)

                context={
                    'admin':admin,
                    'chat_group1':chat_group1,
                    'my_message':my_message,
                }
                return render(request,'human_resource/chat/index1.html',context)

            context={
                    'chat_group':all_chate_team,
                        'admin':admin,
                        'my_message':my_message,
                }
            return render(request,'human_resource/chat/index.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def hr_chat_profile(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            chat_employ=employ.objects.get(pk=id)
            context={
                'admin':admin,
                'chat_employ':chat_employ,
            }
            return render(request,'human_resource/chat/profile.html',context)



   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def hr_chat_pepol(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
                users = User.objects.get(id=request.user.id)
                re_employ=employ.objects.get(user=users)
                admin = re_employ
                chat_employ=employ.objects.get(pk=id)
                user=User.objects.get(pk=request.user.id)
                me=employ.objects.get(user=user)
                
                all_message=chatbot.objects.filter(Q(Q(me_with=chat_employ) | Q(me=chat_employ)) & Q(Q(me_with=me) | Q(me=me)))
                if request.method == 'POST':
                    me_with=employ.objects.get(pk=id)
                    me=me
                    message=request.POST.get('mess')
                    newmess=chatbot.objects.create(me_with=me_with,me=me,message=message)
                    if newmess:
                        return redirect('hr_chat_pepol',id)
                context={
                    'chat_employ':chat_employ,
                    'message':all_message,
                    'id':id,
                    'me':me,
                    'admin':admin,
                }
                return render(request,'human_resource/chat/chat.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  

def hr_all_user(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            me_with=exploreU
            my_message=chatbot.objects.filter(me_with=me_with)
            admin = exploreU
            chat_group1=employ.objects.filter(~Q(user=curretnUser))
            context={
                'admin':admin,
                'my_message':my_message,
                'chat_group2':chat_group1,
            }
            return render(request,'human_resource/chat/index2.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def hr_check_mess(request,id):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            req_messages=chatbot.objects.get(pk=id)
            req_messages.checked=True
            req_messages.save()
            emp_id=req_messages.me_with.id

            return redirect("hr_chat_pepol",emp_id)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
# ------------------------------- end chat ---------------------------------


# ---------------------- Profile ------------------------

def hr_user_Profile(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            context= {
                'admin':admin,
            }
            return render(request,'human_resource/profile/show_profile.html',context)


   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def hr_edit_Profile(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            context= {
                'admin':admin,
            }
            
            if request.method == 'POST':
                admin.about = request.POST.get('about')
                admin.phone1 = request.POST.get('phone1')
                admin.phone2 = request.POST.get('phone2')
                admin.address = request.POST.get('address')
                admin.facebook = request.POST.get('facebook')
                admin.telegram = request.POST.get('telegram')
                admin.instagram = request.POST.get('instagram')
                users.first_name = request.POST.get('first_name')
                users.last_name = request.POST.get('last_name')
                users.email = request.POST.get('email')
                admin.save()
                users.save()
                messages.success(request,'Your profile has been updated successfully. ')
                return redirect('hr_user-Profile')
            return render(request,'human_resource/profile/edit_profile.html',context)

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def hr_chage_password(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            form = passwordform(request.user)
            if request.method == 'POST':
                form = passwordform(request.user, request.POST)
                if form.is_valid():
                    user = form.save()
                    update_session_auth_hash(request, user)  # Important!
                    messages.success(
                        request, 'Your password was successfully updated!')
                    return redirect('hr_user-Profile')
                else:
                    messages.error(request, 'Please correct the error below.')
            else:
                form = passwordform(request.user)
            context = {
                'form': form,
                'admin':admin,
                }
            return render(request,'human_resource/profile/chage_pass.html',context)

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  
def hr_chage_profile_pic(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            context= {
                'admin':admin,
            }
            if len(request.FILES.get('newimg', "")) != 0:
                
                admin.profile_pic.delete()
                admin.profile_pic = request.FILES.get('newimg', "")
                admin.save()
                messages.success(request,'Your profile picture has been updated successfully.')
                return redirect('hr_user-Profile')
            else:
                return render(request,'human_resource/profile/change_profile_pic.html',context)

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def delete_profile_pic(request):
    try:
        if request.user.groups.all()[0].name == 'Human_Resource':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            if len(admin.profile_pic) != 0:
                admin.profile_pic.delete()
                return redirect('hr_user-Profile')
            return render(request,)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
