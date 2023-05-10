from django.shortcuts import render,redirect
from Store_manager.models import *
from django.db.models import Q
from django.contrib.auth.models import User, Group
from Department_Head.models import *
from django.contrib import messages
from django.shortcuts import render,redirect
from itertools import chain
# Create your views here.

def home(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            allDep=department.objects.all()
            deptLength = allDep.__len__()
            allstores=allStore.objects.all()
            allDep=department.objects.all()
            allemp=employ.objects.all()
            emplength=allemp.__len__()
            storeLength=allstores.__len__()
            context={
                'deptLength': deptLength,
                'allstores':allstores,
                'allDep':allDep,
                'emplength':emplength,
                'allemp':allemp,
                'storeLength':storeLength,
            }
            return render(request,'Company_Admin/Dashboard/index.html',context)
                        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
   

def user_profile(request):
    
    return render(request,'Company_Admin/EditProfile/show_profile.html')
def deparetment_dashboard(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            allDep=department.objects.all()
            deptLength = allDep.__len__()
            allstores=allStore.objects.all()
            allDep=department.objects.all()
            allemp=employ.objects.all()
            emplength=allemp.__len__()
            storeLength=allstores.__len__()
            context={
                'deptLength': deptLength,
                'allstores':allstores,
                'allDep':allDep,
                'emplength':emplength,
                'allemp':allemp,
                'storeLength':storeLength,
            }
            
            return render(request,'Company_Admin/Dashboard/departments.html',context)

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def employees_dashboard(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            allDep=department.objects.all()
            deptLength = allDep.__len__()
            allstores=allStore.objects.all()
            allDep=department.objects.all()
            allemp=employ.objects.all()
            emplength=allemp.__len__()
            storeLength=allstores.__len__()
            context={
                'deptLength': deptLength,
                'allstores':allstores,
                'allDep':allDep,
                'emplength':emplength,
                'allemp':allemp,
                'storeLength':storeLength,
            }
            return render(request,'Company_Admin/Dashboard/employees.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
#----------------- MANAGE EMPLOYEE ---------------#
def manage_employee(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':

            allEmployees = employ.objects.all()
            context = {
                'all_emplyees': allEmployees
            }

            return render(request,'Company_Admin/ManageEmployee/index.html', context)

        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def item_in_employee(request,id):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':

            item_rec_emp=employ.objects.get(id=id)
            Request_by=item_rec_emp.Full_Name
            all_emp_request_in_me=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(Company_Admin_Action="Approved") & Q(Recival_status_by_Employer='Received'))  
            
            context={
            'all_emp_request_in_me':all_emp_request_in_me,
            'Request_by':Request_by,
            }
            return render(request,'Company_Admin/ManageEmployee/item_in_employee.html',context)

        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
#----------------- END of manage Employee ---------------#


#----------------- DEPARTMENTS ---------------#

def departments(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':

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
            context={
                'all_dept': all_depts,
                'data':data,
            }
            
            return render(request,'Company_Admin/Departments/index.html', context)

        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def add_new_department(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            DeptHead = employ.objects.filter(role = 'Company_Admin')
            
            context = {
                "departmentHeads" : DeptHead
            }
            if request.method == 'POST':
                departmentName = request.POST.get('departmentName')
                departmentDescription = request.POST.get('departmentDescription')
                
                dept = department.objects.create(departmentName = departmentName,departmentDescription=departmentDescription)
                if dept:
                    messages.success(request,'You Have Successfully added new department.')
                    
                return redirect('departments')

            return render(request,'Company_Admin/Departments/add_new_department.html', context)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def item_in_each_department(request,id):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            req_dep=department.objects.get(pk=id)
            dep_head=req_dep.departmentHead
            re_employ=employ.objects.get(Full_Name=dep_head)
            print(re_employ)
            checkd_by=re_employ
            Request_by=re_employ.Full_Name
            requ_by_dept_recv=dept_request_form1_permanent.objects.filter (Q(Request_by=Request_by) & Q(Store_Keeper_Action="Allowed") & Q(Company_Admin_Action="Approved") & Q(Recival_status_by_Employer='Received') ).order_by("-id") 
            requ_by_emp_recv=employe_request_form1_permanent.objects.filter(Q(checkd_by=checkd_by) & Q(Store_Keeper_Action='Allowed') & Q(Company_Admin_Action="Approved") & Q(Recival_status_by_Employer='Received'))  
            all_receved_req=list(chain(requ_by_dept_recv, requ_by_emp_recv))
            context={
                
                'all_receved_req':all_receved_req,
            }
            
            return render(request,'Company_Admin/Departments/department_details.html', context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def set_dept_head(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            if request.method =="POST":
                dept_id=request.POST.get('departmentId')
                Company_Admin=request.POST.get('dept_head')
                update_dept=department.objects.get(id=dept_id)
                update_dept.departmentHead = Company_Admin
                update_dept.save()
                print("dept_id",dept_id)
                print("Company_Admin",Company_Admin)
            return redirect('department-details',dept_id)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def department_delete(request,id):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            tobedeleted = department.objects.filter(pk=id).delete()
            if tobedeleted:
                
                messages.success(request,'You Have Successfully deleted the department')
                return redirect('departments')
    
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  

#----------------- END of Departments ---------------#


#----------------- VENDORS ---------------#
def vendors(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            allVendors = vendor.objects.all()
            context = {
                'allVendors': allVendors
            }
            return render(request,'Company_Admin/Vendors/index.html',context)

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def vendor_detail(request,id):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            selectedVendor = vendor.objects.get(pk=id)
            context = {
                'selectedVendor': selectedVendor
            }
            return render(request,'Admin/Vendors/vendor_details.html',context)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def add_new_vendor(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
        
            if request.method == 'POST':
                # vendorCode = request.POST.get('vendorCode')
                vendorName = request.POST.get('vendorName')
                vendorProducts = request.POST.get('vendorProducts')
                vendorOrigin = request.POST.get('vendorOrigin')
                vendorType = request.POST.get('vendorType')

                ven = vendor.objects.create(vendorName=vendorName,vendorProducts=vendorProducts,vendorOrigin=vendorOrigin,vendorType=vendorType)
                if ven:
                    messages.success(request,'You Have Successfully added new vendor.')
                    
                return redirect('vendors')

            return render(request, 'Company_Admin/Vendors/add_new_vendor.html')
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')


#----------------- END of VENDORS ---------------#

#----------------- ROLE ---------------#

def role(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            allRoles = allRole.objects.all()
            context={
                'allRoles': allRoles
            }
            return render(request,'Company_Admin/Role/role_details.html',context)

        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
#----------------- END of ROLE ---------------#


#----------------- STORE ---------------#
def store(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            stores = allStore.objects.all()
            context ={
                'stores': stores
            }
            return render(request,'Company_Admin/Store/index.html', context)
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def store_details(request,id):
    store=allStore.objects.get(pk=id)
    all_category = Catagory.objects.filter(store=id)
    all_category.storeId = id
    storeKeepers = employ.objects.filter(role = 'Store_Manager')
    context = {
        'all_category': all_category,
        'storeId':id,
        'store':store,

        
        'storeKeepers': storeKeepers
    }
    if request.method == "POST":
        new_store_name=request.POST.get('store_name')
        store.storeName =new_store_name
        store.save()
        print(new_store_name)
    return render(request,"Company_Admin/Store/store_detail.html", context)

def delete_store(request,id):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            allStore.objects.get(pk=id).delete()
            return redirect('store')
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
def cat_item_detail(request,id):
    return render(request,'Company_Admin/Categories/index.html')    
def add_new_store(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            storeKeepers = employ.objects.filter(role = 'Store_Manager')
            context={
                'storeKeepers': storeKeepers
            }

            if request.method == 'POST':
                storeName = request.POST.get('storeName')
                storeDescription = request.POST.get('storeDescription')
                
                storeLocation = request.POST.get('storeLocation')


                addedStore = allStore.objects.create(storeName=storeName,storeDescription=storeDescription,storeLocation=storeLocation)
                if addedStore:
                    return redirect('store')
                
            return render(request, 'Company_Admin/Store/add_new_store.html', context)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')

def store_manager_update(request,id):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            store=allStore.objects.get(id=id)
            if request.method == "POST":
                new_store_keeper=request.POST.get("store_keeper")
                store.storeKeeper=new_store_keeper
                store.save()
                print("This is store manager",new_store_keeper)
            return redirect('store-details',id)
        def cat_item_detail(request,id):
            category = Catagory.objects.get(pk=id)
            context={
                'category':category
            }
            return render(request, 'Company_Admin/Store/cat_item_details.html',context)

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
#----------------- End OF STORE ---------------#

def reports(request):
    return render(request,'Company_Admin/Reports/index.html')

def chat(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            chat_group=employ.objects.all()
            if request.method == 'POST':
                user=request.POST.get('serach')
                serch=User.objects.get(username=user)
                chat_group1=employ.objects.get(user=serch)
        
                context={
                    
                    'chat_group1':chat_group1,
                }
                return render(request,'Company_Admin/chat/index1.html',context)
            context={
            
                'chat_group':chat_group,
            }
            return render(request,'Company_Admin/chat/index.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def chat_pepol(request,id):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            chat_employ=employ.objects.get(pk=id)
            me=employ.objects.get(pk=request.user.id)
            all_message=chatbot.objects.filter(Q(Q(me_with=chat_employ) | Q(me=chat_employ)) & Q(Q(me_with=me) | Q(me=me)))
            if request.method == 'POST':
                me_with=employ.objects.get(pk=id)
                me=me
                message=request.POST.get('mess')
                newmess=chatbot.objects.create(me_with=me_with,me=me,message=message)
                if newmess:
                    return redirect('admin-chat_people',id)
            context={
                'chat_employ':chat_employ,
                'message':all_message,
                'id':id,
                'me':me
            }
            return render(request,'Company_Admin/chat/chat.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  
def chat_profile(request,id):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            chat_employ=employ.objects.get(pk=id)
            context={
                'chat_employ':chat_employ,
            }
            return render(request,'Company_Admin/chat/profile.html',context)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def send_message(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            me=request.user
            if request.method == 'POST':
              pass
            return redirect('admin-chat_people')


        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def Purchase_item(request):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            all_list_item=form2permanent.objects.all()
            context={
                'all_list_item':all_list_item
            }
            return render(request,'Company_Admin/Purchase_item/Approve_purchase_item.html',context)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def admin_respons(request,id):
    try:
        if request.user.groups.all()[0].name == 'Company_Admin':
            req_order=form2permanent.objects.get(pk=id)
            full_name=req_order.form1per.Request_by
            req_emp=employ.objects.get(Full_Name=full_name)
            context={
                'req_order':req_order,
                'req_emp':req_emp,
            }
            if 'approve' in request.POST:
                note=request.POST.get('note')
                req_order.Admin_response=note
                req_order.Admin_Appruval='Approved'
                req_order.save()
                return redirect('Purchase_item')
            elif 'reject' in request.POST:
                note=request.POST.get('note')
                req_order.Admin_response=note
                req_order.Admin_Appruval='Reject'
                req_order.save()
                return redirect('Purchase_item')
            return render(request,'Company_Admin/Purchase_item/admin_respons.html',context)

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    