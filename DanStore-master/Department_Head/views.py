from django.shortcuts import render,redirect
from django.contrib import messages
from Store_manager.models import *
from .models import *
from itertools import chain
from django.db.models import Q
def dept_head(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            me_with=exploreU
            admin=exploreU
            my_message=chatbot.objects.filter(Q(me_with=me_with) & Q(checked=False))
            dept_head=exploreU.Full_Name
            dept_name=department.objects.get(departmentHead=dept_head)
            indep=dept_name.departmentName
            exploreU.inDepartment=dept_name.departmentName
            exploreU.save()
            all_emp=employ.objects.filter(inDepartment=indep)
            all_request=employe_request_form1_permanent.objects.filter(Q(checkd_by=exploreU) & Q(dept_head_Action="Pending"))
            No_pending_req=all_request.count()
            context = {
                'userData' : exploreU,
                'dept_name':dept_name,
                'all_emp':all_emp,
                'No_pending_req':No_pending_req,
                'all_my_message_':my_message,
                'admin':admin,
            }
            return render(request,'Department_head/index.html', context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
  

def add_employe(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            me_with=exploreU
            admin=exploreU
            my_message=chatbot.objects.filter(me_with=me_with)
            
            dept_head=exploreU.Full_Name
            dept_name=department.objects.get(departmentHead=dept_head)
            allEmps = employ.objects.filter(Q(role = "Employee") & Q(inDepartment = None))
        
            context = {
                'allEmps' : allEmps,
                'my_message':my_message,
                'admin':admin,
            }
            if request.method == 'POST':
                newemp=request.POST.get('emp')
                check=request.POST.get('check')
                newadd_emp=employ.objects.get(id=newemp)
                print("--------------------")
                print(newadd_emp)
                print("--------------------")
                newadd_emp.inDepartment=dept_name.departmentName
                if check:
                    newadd_emp.Thechnologist=True
                newadd_emp.save()
                return redirect('dept-dashboard')
            return render(request,'Department_head/add_employe.html',context)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
   
def add_emp(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
           
            if request.method == 'POST':
                newempl=request.POST.get('emp')
                print("----------------")
                print(newempl)
                return redirect('dept-dashboard')


   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  
def cheek_request(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            me_with=exploreU
            admin=exploreU
            my_message=chatbot.objects.filter(me_with=me_with)
            all_request=employe_request_form1_permanent.objects.filter(Q(checkd_by=exploreU) & ~Q(Recival_status_by_Employer='Not_Received') )
            context={
                'all_request':all_request,
                'my_message':my_message,
                "admin":admin,
            }
            return render(request,'Department_head/check_request.html',context)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
  
def dept_approved(request,id):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            me_with=exploreU
            my_message=chatbot.objects.filter(me_with=me_with)
            emp_request=employe_request_form1_permanent.objects.get (Q(checkd_by=exploreU) & Q(pk=id))
            emp_request.dept_head_Action="Approved"
            emp_request.save()
            return redirect('check_request')
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
   

def dept_reject(request,id):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            me_with=exploreU
            my_message=chatbot.objects.filter(me_with=me_with)
            emp_request=employe_request_form1_permanent.objects.get (Q(checkd_by=exploreU) & Q(pk=id))
            emp_request=employe_request_form1_permanent.objects.get (Q(checkd_by=exploreU) & Q(pk=id))
            emp_request.dept_head_Action="Rejected"
            emp_request.save()
            return redirect('check_request')

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
    
def unreceived_request(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            me_with=exploreU
            admin=exploreU
            my_message=chatbot.objects.filter(me_with=me_with)
            
            re_employ=employ.objects.get(user=curretnUser)
            admin = re_employ
            checkd_by=re_employ
            Request_by=re_employ.Full_Name
            requ_by_dept=dept_request_form1_permanent.objects.filter (Q(Request_by=Request_by) | Q(checkd_by=checkd_by)).order_by("-id") 
            requ_by_emp=employe_request_form1_permanent.objects.filter(Q(checkd_by=checkd_by) & Q(dept_head_Action="Approved")).order_by("-id") 
            all_unreseved_req=list(chain(requ_by_dept, requ_by_emp))
            context={
                'admin':admin,
                'all_unreseved_req':all_unreseved_req,
                'my_message':my_message
            }
            return render(request,'Department_head/unreceived_request.html',context)
            
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
   

def rejected_emp_request(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            me_with=exploreU
            admin=exploreU
            my_message=chatbot.objects.filter(me_with=me_with)
            all_request=employe_request_form1_permanent.objects.filter(checkd_by=exploreU)
            context={
                'all_request':all_request,
                'my_message':my_message,
                'admin':admin,
            }
            return render(request,'Department_head/Rejected_request.html',context)

        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')

  

# ----------------------- store add file request -------------------
def dept_request(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            me_with=exploreU
            my_message=chatbot.objects.filter(me_with=me_with)
            admin = exploreU
            Request_by=exploreU.Full_Name
            Department=(exploreU.inDepartment)
            request_store=(exploreU.accessStore)
            context={
                'admin':admin,
                'my_message':my_message,
            }
            checkd_by = exploreU

            if dept_request_form1.objects.filter(Request_by=Request_by).count() !=0:
                dept_request_form1.objects.filter(Request_by=Request_by).delete()
                form1=dept_request_form1.objects.create(request_store=request_store,Request_by=Request_by,Department=Department,checkd_by=checkd_by)
            
            else:
                form1=dept_request_form1.objects.create(request_store=request_store,Request_by=Request_by,Department=Department,checkd_by=checkd_by)
                
            return render(request,'Department_head/make_request.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
 
def dept_request2(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            Request_by=re_employ.Full_Name
            form1=dept_request_form1.objects.filter(Request_by=Request_by)
            
            newform=form1[0]
            
            emp_req=dept_request_form2.objects.filter(dept_request_form1=newform)
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
                form2=dept_request_form2.objects.create(dept_request_form1=form1,Description=Description,unit=unit,req_qty=req_qty,Remark=Remark)
            if form2:
                print("created form 2")
            return render(request,'Department_head/make_request.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
    

def dept_complet_request(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            Request_by=re_employ.Full_Name
            form1=dept_request_form1.objects.get(Request_by=Request_by)
            Request_by=form1.Request_by
            Department=form1.Department
            request_store=form1.request_store
            checkd_by=form1.checkd_by
            all_items=dept_request_form2.objects.filter(dept_request_form1=form1)
            for item in all_items:
                Description=item.Description
                unit=item.unit
                req_qty=item.req_qty
                Remark=item.Remark
                dept_request_form1_permanent.objects.create( 
                    Request_by=Request_by,
                    Department=Department,
                    request_store=request_store,
                    checkd_by=checkd_by,
                    Description=Description,
                    unit=unit,
                    req_qty=req_qty,
                    Remark=Remark,)
            return redirect('unreceived-request')
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')

  

def all_item_taken_by(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            checkd_by=re_employ
            Request_by=re_employ.Full_Name
            requ_by_dept_recv=dept_request_form1_permanent.objects.filter (Q(Request_by=Request_by) & Q(Store_Keeper_Action="Allowed") & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Received') ).order_by("-id") 
            requ_by_emp_recv=employe_request_form1_permanent.objects.filter(Q(checkd_by=checkd_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Received'))  
            
            all_receved_req=list(chain(requ_by_dept_recv, requ_by_emp_recv))
            context={
                'admin':admin,
                'all_receved_req':all_receved_req,
            }
            return render(request,'Department_head/all_item_taken_by.html',context)

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
   
# ------------------------ Chat ----------------------------------------------

def dept_chat(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
          
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
                return render(request,'Department_head/chat/index1.html',context)

            context={
                    'chat_group':all_chate_team,
                    'admin':admin,
                    'my_message':my_message,
                }
            return render(request,'Department_head/chat/index.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')

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
        return render(request,'Department_head/chat/index1.html',context)

    context={
            'chat_group':all_chate_team,
             'admin':admin,
             'my_message':my_message,
        }
    return render(request,'Department_head/chat/index.html',context)
def dept_chat_profile(request,id):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            chat_employ=employ.objects.get(pk=id)
            context={
                'admin':admin,
                'chat_employ':chat_employ,
            }
            return render(request,'Department_head/chat/profile.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')

   
def dept_chat_pepol(request,id):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
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
                    return redirect('dept_chat_pepol',id)
            context={
                'chat_employ':chat_employ,
                'message':all_message,
                'id':id,
                'me':me,
                'admin':admin,
            }
            return render(request,'Department_head/chat/chat.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')

   
def all_user(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            me_with=exploreU
            my_message=chatbot.objects.filter(me_with=me_with)
            admin = exploreU
            chat_group1=employ.objects.all()
            context={
                'admin':admin,
                'my_message':my_message,
                'chat_group2':chat_group1,
            }
            return render(request,'Department_head/chat/index2.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')

    
def dept_check_mess(request,id):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':

            req_messages=chatbot.objects.get(pk=id)
            req_messages.checked=True
            req_messages.save()
            emp_id=req_messages.me_with.id

            return redirect("dept_chat_pepol",emp_id)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
# ------------------------------- end chat ---------------------------------

def role(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
         return render(request,'Department_head/role.html')
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')



# ---------------------- Profile ------------------------

def user_Profile(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
      
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            context= {
                'admin':admin,
            }
            return render(request,'Department_head/profile/show_profile.html',context)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')


def edit_Profile(request):
    try:
        if request.user.groups.all()[0].name == 'Dept_Head':
           
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
        if request.user.groups.all()[0].name == 'Dept_Head':

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
        if request.user.groups.all()[0].name == 'Dept_Head':
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
        if request.user.groups.all()[0].name == 'Dept_Head':
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
    
    