from django.shortcuts import render,redirect
from django.contrib import messages
from Store_manager.models import * 
from django.db.models import Q
from .form import *
from django.contrib.auth import update_session_auth_hash
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 


def employe_view(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            Request_by=re_employ.Full_Name
            all_emp_request=employe_request_form1_permanent.objects.filter(Request_by=Request_by)
            all_emp_request_in_me=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Received'))  
            all_emp_request_retun=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Returned'))  
            all_emp_request_reject=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Reject') | Q(dept_head_Action="Rejected") | Q(Recival_status_by_Employer='Not_Received'))  
            all_emp_request_pending=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & ~Q(Store_Keeper_Action='Reject') & ~Q(Recival_status_by_Employer='Received'))  
            all_emp_request_pending1=[]
            for i in all_emp_request_pending:
                if i.Recival_status_by_Employer == 'Not_Received':
                    pass
                elif i.Recival_status_by_Employer == 'Returned':
                    pass
                else:
                    all_emp_request_pending1.append(i)
            total_pending=(len(all_emp_request_pending1))

            context={
                'all_emp_request_pending':all_emp_request_pending,
                'all_emp_request_in_me':all_emp_request_in_me,
                'all_emp_request_retun':all_emp_request_retun,
                'all_emp_request_reject':all_emp_request_reject,
                'all_emp_request':all_emp_request,
                'admin':admin,
                'total_pending':total_pending,
            } 
            return render(request,'employe/index.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def emp_request(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':

            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            Request_by=re_employ.Full_Name
            Department=(re_employ.inDepartment)
            request_store=(re_employ.accessStore)
            context={
                'admin':admin,
            }
            checkd_by = employ.objects.get(Q(role = "Dept_Head") & Q(inDepartment=Department))
            if employe_request_form1.objects.filter(Request_by=Request_by).count() !=0:
                employe_request_form1.objects.filter(Request_by=Request_by).delete()
                form1=employe_request_form1.objects.create(request_store=request_store,Request_by=Request_by,Department=Department,checkd_by=checkd_by)
            else:
                form1=employe_request_form1.objects.create(request_store=request_store,Request_by=Request_by,Department=Department,checkd_by=checkd_by)
            form1=employe_request_form1.objects.filter(Request_by=Request_by)
            new_form1=form1[0]
            if request.method == "POST":
                employe_request_form2.objects.create(employe_request_form1=new_form1)
            return render(request,'employe/request.html',context)
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def emp_request2(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
            user=request.user
            emp=employ.objects.get(user=user)
            Request_by=emp.Full_Name
            form1=employe_request_form1.objects.filter(Request_by=Request_by)
            
            newform=form1[0]
            
            emp_req=employe_request_form2.objects.filter(employe_request_form1=newform)
            context={
                'emp_req':emp_req,
            }
            if form1:
                form1=form1[0]
            if request.method == 'POST':
                Description=request.POST.get("desc")
                unit=request.POST.get("unit")
                req_qty=request.POST.get("qty")
                Remark=request.POST.get("remark")
                form2=employe_request_form2.objects.create(employe_request_form1=form1,Description=Description,unit=unit,req_qty=req_qty,Remark=Remark)
            if form2:
                print("created form 2")
            return render(request,'employe/request.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def complet_request(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':

            user=request.user
            emp=employ.objects.get(user=user)
            Request_by=emp.Full_Name
            form1=employe_request_form1.objects.get(Request_by=Request_by)
            Request_by=form1.Request_by
            Department=form1.Department
            request_store=form1.request_store
            checkd_by=form1.checkd_by
            all_items=employe_request_form2.objects.filter(employe_request_form1=form1)
            for item in all_items:
                Description=item.Description
                unit=item.unit
                req_qty=item.req_qty
                Remark=item.Remark
                employe_request_form1_permanent.objects.create( 
                    Request_by=Request_by,
                    Department=Department,
                    request_store=request_store,
                    checkd_by=checkd_by,
                    Description=Description,
                    unit=unit,
                    req_qty=req_qty,
                    Remark=Remark,)
            return redirect('employe_dashboard')
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
 
    

def reste_request_form(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
            user=request.user
            emp=employ.objects.get(user=user)
            Request_by=emp.Full_Name
            form1=employe_request_form1.objects.get(Request_by=Request_by)
            employe_request_form2.objects.filter(employe_request_form1=form1).delete()

            return render(request,'employe/request.html',)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def view_request(request,id):
    try:
        if request.user.groups.all()[0].name == 'Employe':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            Request_by=re_employ.Full_Name
            all_emp_request=employe_request_form1_permanent.objects.get(pk=id)  
            context={
                'item':all_emp_request,
                'admin':admin,
            } 
            return render(request,'employe/view_request.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    



def accept_approveal(request,id):
    try:
        if request.user.groups.all()[0].name == 'Employe':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            taken_by=re_employ.Full_Name
            all_emp_request=employe_request_form1_permanent.objects.get(pk=id)  
            item_name=all_emp_request.Description
            num=int(str(all_emp_request.req_qty))
            req_item=Item.objects.get(item_name=item_name)
            in_stock=int(str(req_item.total_item_in_Stok))
            if in_stock >= num:
                after_rece = str(in_stock-num)
            else:
                pass
            req_item.total_item_in_Stok = after_rece
            ItemHistory.objects.create(Item=req_item,Amount=num,Action='Removed',Other_Reseaon='Given To employee',taken_by=taken_by)
            req_item.save()
            all_emp_request.Recival_status_by_Employer="Received"
            all_emp_request.save()
            return redirect('employe_dashboard')
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def cancel_request(request,id):
    try:
        if request.user.groups.all()[0].name == 'Employe':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            all_emp_request=employe_request_form1_permanent.objects.get(pk=id)  
            all_emp_request.Recival_status_by_Employer="Not_Received"
            all_emp_request.save()
            return redirect('employe_dashboard')   
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def pending_item(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            Request_by=re_employ.Full_Name
            all_emp_request_in_me=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Received'))  
            all_emp_request_retun=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Returned'))  
            all_emp_request_reject=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Reject') | Q(dept_head_Action="Rejected") | Q(Recival_status_by_Employer='Not_Received'))  
            all_emp_request_pending=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & ~Q(Store_Keeper_Action='Reject') & ~Q(Recival_status_by_Employer='Received'))     
            all_emp_request_pending1=[]
            for i in all_emp_request_pending:
                if i.Recival_status_by_Employer == 'Not_Received':
                    pass
                elif i.Recival_status_by_Employer == 'Returned':
                    pass
                else:
                    all_emp_request_pending1.append(i)
            total_pending=(len(all_emp_request_pending1))
            context={
                'all_emp_request_pending':all_emp_request_pending1,
                'all_emp_request_in_me':all_emp_request_in_me,
                'all_emp_request_retun':all_emp_request_retun,
                'all_emp_request_reject':all_emp_request_reject,
                'total_pending':total_pending,
                'admin':admin,
            } 
            return render(request,'employe/pending.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def total_item_in_me(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            Request_by=re_employ.Full_Name
            all_emp_request_in_me=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Received'))  
            
            all_emp_request_retun=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Returned'))  
            all_emp_request_reject=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Reject') | Q(dept_head_Action="Rejected") | Q(Recival_status_by_Employer='Not_Received'))  
            all_emp_request_pending=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & ~Q(Store_Keeper_Action='Reject') & ~Q(Recival_status_by_Employer='Received'))     
            all_emp_request_pending1=[]
            for i in all_emp_request_pending:
                if i.Recival_status_by_Employer == 'Not_Received':
                    pass
                elif i.Recival_status_by_Employer == 'Returned':
                    pass
                else:
                    all_emp_request_pending1.append(i)
            total_pending=(len(all_emp_request_pending1))
            context={
                'all_emp_request_pending':all_emp_request_pending,
                'all_emp_request_in_me':all_emp_request_in_me,
                'all_emp_request_retun':all_emp_request_retun,
                'all_emp_request_reject':all_emp_request_reject,
                'total_pending':total_pending,
                'admin':admin,
            } 
            return render(request,'employe/totali_item_in_me.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def Returned_item(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
 
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            Request_by=re_employ.Full_Name
            all_emp_request_in_me=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Received'))  
            all_emp_request_retun=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Returned'))  
            all_emp_request_reject=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Reject') | Q(dept_head_Action="Rejected") | Q(Recival_status_by_Employer='Not_Received'))  
            all_emp_request_pending=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & ~Q(Store_Keeper_Action='Reject') & ~Q(Recival_status_by_Employer='Received'))     
            all_emp_request_pending1=[]
            for i in all_emp_request_pending:
                if i.Recival_status_by_Employer == 'Not_Received':
                    pass
                elif i.Recival_status_by_Employer == 'Returned':
                    pass
                else:
                    all_emp_request_pending1.append(i)
            total_pending=(len(all_emp_request_pending1))
            

            context={
            'all_emp_request_pending':all_emp_request_pending,
                'all_emp_request_in_me':all_emp_request_in_me,
                'all_emp_request_retun':all_emp_request_retun,
                'all_emp_request_reject':all_emp_request_reject,
                'admin':admin,
                'total_pending':total_pending,
            } 
            return render(request,'employe/Returned_item.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def Rejected_Canceld(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            Request_by=re_employ.Full_Name
            all_emp_request_in_me=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Received'))  
            all_emp_request_retun=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Returned'))  
            all_emp_request_reject=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Reject') | Q(dept_head_Action="Rejected") | Q(Recival_status_by_Employer='Not_Received'))  
            all_emp_request_pending=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & ~Q(Store_Keeper_Action='Reject') & ~Q(Recival_status_by_Employer='Received'))  
            all_emp_request_pending1=[]
            for i in all_emp_request_pending:
                if i.Recival_status_by_Employer == 'Not_Received':
                    pass
                elif i.Recival_status_by_Employer == 'Returned':
                    pass
                else:
                    all_emp_request_pending1.append(i)
            total_pending=(len(all_emp_request_pending1))
            context={
                'all_emp_request_pending':all_emp_request_pending,
                'all_emp_request_in_me':all_emp_request_in_me,
                'all_emp_request_retun':all_emp_request_retun,
                'all_emp_request_reject':all_emp_request_reject,
                'admin':admin,
                'total_pending':total_pending,
            } 
            return render(request,'employe/Rejected_Canceld.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  

# ---------------------- Profile ------------------------

def user_Profile(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            context= {
                'admin':admin,
            }
            return render(request,'employe/profile/show_profile.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def edit_Profile(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
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
                return redirect('emp_user-Profile')
            return render(request,'employe/profile/edit_profile.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  

def chage_password(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
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
                    return redirect('emp_user-Profile')
                else:
                    messages.error(request, 'Please correct the error below.')
            else:
                form = passwordform(request.user)
            context = {
                'form': form,
                'admin':admin,
                }
            return render(request,'employe/profile/chage_pass.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def emp_chage_profile_pic(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
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
                return redirect('emp_user-Profile')
            else:
                return render(request,'employe/profile/change_profile_pic.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def delete_profile_pic(request):
    try:
        if request.user.groups.all()[0].name == 'Employe':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            context= {
                'admin':admin,
            }
            if len(admin.profile_pic) != 0:
                admin.profile_pic.delete()
                return redirect('emp_user-Profile')
            return render(request,)

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  

class emp_deliverd_item(View):
   def get(self, request,id, *args, **kwargs,):
    item=employe_request_form1_permanent.objects.get(id=id)
    req=item.Request_by
    req_em=employ.objects.get(Full_Name=req)
    data={
        'item':item,
        'req_em':req_em,
    }
    open('templates/temp.html', "w").write(render_to_string('employe/pdf_item_data.html',data ))
    pdf = html_to_pdf('temp.html')
    return HttpResponse(pdf, content_type='application/pdf')