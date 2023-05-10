from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, reverse
from .form import *
from .models import chatbot
from .models import *
from itertools import chain
from Department_Head.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import View
from Store_manager import models
from .process import html_to_pdf 
from django.core.exceptions import ObjectDoesNotExist


#Creating a class based view
def store_dashboard(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
                id=(request.user.id)
                user=User.objects.get(id=id)
                re_emp=employ.objects.get(user=user)
                re_Store=allStore.objects.get(storeKeeper=re_emp.Full_Name)
                try:
                    all_catagory = Catagory.objects.filter(store=re_Store)
                except Catagory.DoesNotExist:
                    all_catagory = None
                context ={
                    'all_catagory':all_catagory,
                    're_emp':re_emp,
                }
                return render(request,'Store_manager/dashboard.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def manage_catagory(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
                id=(request.user.id)
                user=User.objects.get(id=id)
                re_emp=employ.objects.get(user=user)
                re_Store=allStore.objects.get(storeKeeper=re_emp.Full_Name)
                try:
                    all_catagory = Catagory.objects.filter(store=re_Store)
                except Catagory.DoesNotExist:
                    all_catagory = None
                
                context ={
                    'all_catagory':all_catagory,
                    're_emp':re_emp,
                    
                }
                if request.method == 'POST':
                    new_catagory = request.POST.get('catagory')
                    Type_of_Asset=request.POST.get('typeasset')
                    new=Catagory.objects.filter(Catagory_Name=new_catagory)
                    if new.count():
                        
                        messages.error(request,"A category name already exists. Please alter the category name.")
                    else:
                        add_new_catagory=Catagory.objects.create(store=re_Store,Catagory_Name=new_catagory,Type_of_Asset=Type_of_Asset)
                        if add_new_catagory:
                            messages.success(request,"You have added a new category successfully.")
                            return redirect('manage-catagory')
                return render(request,'Store_manager/Catagory/manage_catagory.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
 
def search_catagory(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            id=(request.user.id)
            user=User.objects.get(id=id)
            re_emp=employ.objects.get(user=user)
            if request.method == 'POST':
                serched_catagory_name = request.POST.get('query')
                if serched_catagory_name:
                    try:
                        serched_catagory=Catagory.objects.get(Catagory_Name=serched_catagory_name)

                        context={
                    'serched_catagory':serched_catagory,
                    're_emp':re_emp,
                    }
                    except:
                        try:
                            item_ser=Item.objects.get(item_name=serched_catagory_name)
                            serched_catagory=item_ser.Catagory
                            context={
                            'serched_catagory':serched_catagory
                            }
                        except ObjectDoesNotExist:
                            messages.error(request,"Please type the proper shelf name or Item name.")
                            return redirect('store-dashboard')
                    return render(request,'Store_manager/Catagory/search_catagory.html',context)
                else:
                    messages.error(request,"Please enter shelf name")
                    return redirect('store-dashboard')
            
            return render(request,'Store_manager/Catagory/search_catagory.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def add_new_catagory(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
                id=(request.user.id)
                user=User.objects.get(id=id)
                re_emp=employ.objects.get(user=user)
                all_catagory = Catagory.objects.all()
                context ={
                    'all_catagory':all_catagory,
                    're_emp':re_emp,
                }
                if request.method == 'POST':
                    new_catagory = request.POST.get('catagory')
                    total_item = request.POST.get('totalitem')
                    add_new_catagory=Catagory.objects.create(Catagory_Name=new_catagory,total_item=total_item)
                    
                    if add_new_catagory:
                        messages.success(request,"You have added a new category successfully.")
                return render(request,'Store_manager/Catagory/manage_catagory.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
 
def catagory_detail(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            catagory = Catagory.objects.get(pk=id)
            context={
                'catagory':catagory,
                're_emp':re_emp,
            }
            if request.method == 'POST':
                new_catagory = request.POST.get('catagory')
                catagory.Catagory_Name=new_catagory
                catagory.save()
                if catagory:
                    messages.success(request,"You have update Category Name successfully.")
            return render(request,'Store_manager/Catagory/catagory_detail.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def delete_catagory(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            Catagory.objects.get(pk=id).delete()
            return redirect('manage-catagory')
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def add_item(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            catagory=Catagory.objects.get(pk=id)
            context={
                'catagory':catagory,
                're_emp':re_emp,
            }
            if request.method == 'POST':
                item_name = request.POST.get('itemname')
                amount = request.POST.get('total')
                check=Item.objects.filter(item_name=item_name)
                if check.count():
                    messages.error(request,'Please change the item Name.')
                else:
                    new_item=Item.objects.create(Catagory=catagory,item_name=item_name,total_item_in_Stok=amount)
                    if new_item:
                        ItemHistory.objects.create(Item=new_item,Reason='Other',Action='Add',Amount=amount,Other_Reseaon='currently in store')
                        messages.success(request,"You have added New Item Successfully.")
                        return redirect('catagory-detail' ,id)
            return render(request,'Store_manager/Catagory/catagory_detail.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def item_detail(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
                user_id=(request.user.id)
                user=User.objects.get(id=user_id)
                re_emp=employ.objects.get(user=user)
                item=Item.objects.get(pk=id)
                item_history=ItemHistory.objects.filter(Item=item)
                context={
                    'item':item,
                    'item_history':item_history,
                    're_emp':re_emp
                }
                if request.method == 'POST':
                    new_catagory = request.POST.get('item_name')
                    item.item_name=new_catagory
                    item.save()
                    if item:
                        messages.success(request,"You have update item Name successfully.")
                return render(request,'Store_manager/Catagory/item_detail.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  
def item_delete(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            item=Item.objects.get(pk=id)
            catagory=item.Catagory
            id2=catagory.id
            Item.objects.get(pk=id).delete()
            return redirect('catagory-detail', id2)

        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def add_to_store1(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            re_Store=allStore.objects.get(storeKeeper=re_emp.Full_Name)
            all_oreder=form2permanent.objects.filter(Q(Admin_Appruval='Approved') & Q(Finance_Action='Completed'))
            try:
                all_catagory = Catagory.objects.filter(store=re_Store)
                all_emp=[]
                
                requ_by_dept_recv=dept_request_form1_permanent.objects.filter (Q(request_store=re_Store) & Q(Recival_status_by_Employer="Received")).order_by("-id") 
                requ_by_emp_recv=employe_request_form1_permanent.objects.filter(Q(request_store=re_Store) & Q(Recival_status_by_Employer="Received")).order_by("-id") 
                all_receved_req=list(chain(requ_by_dept_recv, requ_by_emp_recv))
                all_req=[]
                for emp in all_receved_req:
                    if emp.Request_by in all_req:
                        pass
                    else:
                        all_req.append(emp.Request_by)
                for emp in all_req:
                    all_emp.append(employ.objects.get(Full_Name=emp))
            except Catagory.DoesNotExist:
                all_catagory = None
        
            
            if request.method == 'POST':
                res=request.POST.get('reson')
                all_item=Item.objects.all()
                all_orderd=form2permanent.objects.all()
                requ_by_dept_recv=dept_request_form1_permanent.objects.filter (Q(request_store=re_Store) & Q(Recival_status_by_Employer="Received")).order_by("-id") 
                requ_by_emp_recv=employe_request_form1_permanent.objects.filter(Q(request_store=re_Store) & Q(Recival_status_by_Employer="Received")).order_by("-id") 
                all_receved_req=list(chain(requ_by_dept_recv, requ_by_emp_recv))
            
                context={
                    
                    'res':res,
                    'all_item':all_item,
                    'all_orderd':all_orderd,
                    'all_catagory':all_catagory,
                    'all_emp':all_emp,
                    'all_receved_req':all_receved_req,
                    're_emp':re_emp,
                    'all_oreder':all_oreder,

                }
        
                
                return render(request,"Store_manager/Add_to_Store/add_to_store1.html",context)
            return redirect('add-to-store')
   
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def cheeck_request(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            name=exploreU.Full_Name
            store=allStore.objects.get(storeKeeper=name)
            emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            all_unreseved_req=list(chain(emp_request, dep_request))
            context={
                'emp_request':all_unreseved_req,
                're_emp':re_emp,
            }
            return render(request,"Store_manager/cheeck_Request/cheeck_request.html",context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def aproved_request(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            name=exploreU.Full_Name
            store=allStore.objects.get(storeKeeper=name)
            emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            all_unreseved_req=list(chain(emp_request, dep_request))
            context={
                'emp_request':all_unreseved_req,
                're_emp':re_emp,
            }
            return render(request,'Store_manager/cheeck_Request/approved_request.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def Item_Delivery_form(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            name=exploreU.Full_Name
            store=allStore.objects.get(storeKeeper=name)
            emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            all_unreseved_req=list(chain(emp_request, dep_request))
            both_request={}
            for i in all_unreseved_req:
                if i.id == id:
                    both_request=i
            full_name=both_request.Request_by
            req_em=employ.objects.get(Full_Name=full_name)
            
            context={
                'item':both_request,
                'req_em':req_em,
                're_emp':re_emp
            }
            
            return render(request,'Store_manager/cheeck_Request/Item_Delivery_form.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def check_delivered_item(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            name=exploreU.Full_Name
            store=allStore.objects.get(storeKeeper=name)
            emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            all_unreseved_req=list(chain(emp_request, dep_request))
            both_request={}
            for i in all_unreseved_req:
                if i.id == id:
                    both_request=i
            full_name=both_request.Request_by
            Department=both_request.Department
            req_em=employ.objects.get(Full_Name=full_name)
            
            re_dep=department.objects.get(departmentName=Department)
            dep_head=re_dep.departmentHead
            context={
                'item':both_request,
                'req_em':req_em,
                're_emp':re_emp,
                'dep_head':dep_head,
            }
            
            return render(request,'Store_manager/cheeck_Request/check_delivered_item.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def set_item_specifications(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            name=exploreU.Full_Name
            store=allStore.objects.get(storeKeeper=name)
            emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            all_unreseved_req=list(chain(emp_request, dep_request))
            ser_request={}
            if request.method == 'POST':
                Type_of_item=request.POST.get('type')
                Serial_No=request.POST.get('seralNo')
                Unique_Name_No=request.POST.get('uniqueNo')
                try:
                    ser_request=employe_request_form1_permanent.objects.get(id=id)
                except:
                    ser_request=dept_request_form1_permanent.objects.get(id=id)
                ser_request.Type_of_item=Type_of_item
                ser_request.Serial_No=Serial_No
                ser_request.Unique_Name_No=Unique_Name_No
                ser_request.save()
            return redirect('aproved_request')
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def rejected_request(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
                user_id=(request.user.id)
                user=User.objects.get(id=user_id)
                re_emp=employ.objects.get(user=user)
                curretnUser = request.user
                exploreU = employ.objects.get(user = curretnUser)
                name=exploreU.Full_Name
                store=allStore.objects.get(storeKeeper=name)
                emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
                dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
                all_unreseved_req=list(chain(emp_request, dep_request))
                context={
                    'emp_request':all_unreseved_req,
                    're_emp':re_emp,
                }
                return render(request,'Store_manager/cheeck_Request/rejected_request.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def check_in_stok(request,Description):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            req_item_inlower=Description.lower()
            req_item_inupper=Description.capitalize()
            try: 
                order_item=Item.objects.filter(item_name=req_item_inlower)
            except ObjectDoesNotExist:
                try:
                    order_item=Item.objects.filter(item_name=req_item_inupper)
                except ObjectDoesNotExist:
                    order_item=None
            print(order_item)
            for item in order_item: 
                print(item.item_name)
            context={
                'order_item':order_item,
                're_emp':re_emp,
            }
            return render(request,'Store_manager/cheeck_Request/check_in_soke.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def put_message_rejected_request(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            name=exploreU.Full_Name
            store=allStore.objects.get(storeKeeper=name)
            emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            all_unreseved_req=list(chain(emp_request, dep_request))
            for requ in all_unreseved_req:
                if requ.id==id:
                    searchedReq=requ
                    print(searchedReq)
            context={
                'searchedReq':searchedReq,
                're_emp':re_emp,
            }
            
            if request.method == 'POST':
                mess=request.POST.get('store_message')
                id=str(request.POST.get('request_id'))
                for requ in all_unreseved_req:
                    if str(requ.id)==id:
                        searchedReq=requ
                        searchedReq.note=mess
                        searchedReq.Store_Keeper_Action="Reject"
                        searchedReq.save()
                        return redirect('rejected-request')
            return render(request,"Store_manager/cheeck_Request/message1.html",context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def send_message_to_request(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            name=exploreU.Full_Name
            store=allStore.objects.get(storeKeeper=name)
            emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            all_unreseved_req=list(chain(emp_request, dep_request))
            for requ in all_unreseved_req:
                if requ.id==id:
                    searchedReq=requ
                    print(searchedReq)
            context={
                'searchedReq':searchedReq,
                're_emp':re_emp,
            }
            
            return render(request,"Store_manager/cheeck_Request/message.html",context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def store_manage_approve(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            curretnUser = request.user
            exploreU = employ.objects.get(user = curretnUser)
            name=exploreU.Full_Name
            store=allStore.objects.get(storeKeeper=name)
            emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
            all_unreseved_req=list(chain(emp_request, dep_request))
            searchedReq={}
            if request.method == 'POST':
                mess=request.POST.get('store_message')
                id=str(request.POST.get('request_id'))
                order=request.POST.get('order')
                if order == 'on':
                    for requ in all_unreseved_req:
                        if str(requ.id)==id:
                            searchedReq=requ
                            Request_by=searchedReq.Request_by
                            Department=searchedReq.Department
                            checkd_by=searchedReq.checkd_by
                            Description=searchedReq.Description
                            unit=searchedReq.unit
                            req_qty=searchedReq.req_qty
                            Remark=searchedReq.Remark
                            form1=form1permanent.objects.create(Request_by=Request_by,Department=Department,checkd_by=checkd_by)
                            form2=form2permanent.objects.create(form1per=form1,Description=Description,unit=unit,req_qty=req_qty,Remark=Remark,Admin_Appruval='Pending', Finance_Action='Pending',Item_Status='Pending')
                            searchedReq.note=mess
                            searchedReq.Store_Keeper_Action="Allowed"
                            searchedReq.save()
                            if form2:
                               return redirect('list_for_purchase')
                else:
                    for requ in all_unreseved_req:
                        if str(requ.id)==id:
                            searchedReq=requ
                            searchedReq.note=mess
                            searchedReq.Store_Keeper_Action="Allowed"
                            searchedReq.save()
                return redirect('aproved_request')
                
            return render(request,"Store_manager/cheeck_Request/message.html")
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def user_Profile(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            users = User.objects.get(id=request.user.id)
            re_employ=employ.objects.get(user=users)
            admin = re_employ
            context= {
                'admin':admin,
                're_emp':admin,
            }
            return render(request,'Store_manager/profile/show_profile.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def edit_Profile(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
                users = User.objects.get(id=request.user.id)
                re_employ=employ.objects.get(user=users)
                admin = re_employ
                context= {
                    'admin':admin,
                    're_emp':admin,
                }
                if request.method == 'POST':
                    admin.about = request.POST['about']
                    admin.phone1 = request.POST['phone']
                    admin.address = request.POST['address']
                    admin.facebook = request.POST['facebook']
                    admin.telegram = request.POST['telegram']
                    admin.instagram = request.POST['instagram']
                    users.first_name = request.POST['first_name']
                    users.last_name = request.POST['last_name']
                    users.email = request.POST['email']
                    admin.save()
                    users.save()
                    messages.success(request,'Your profile has been updated successfully. ')
                    return redirect('user-Profile')
                return render(request,'Store_manager/profile/edit_profile.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def chage_password(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
                form = passwordform(request.user)
                if request.method == 'POST':
                    form = passwordform(request.user, request.POST)
                    if form.is_valid():
                        user = form.save()
                        update_session_auth_hash(request, user)  # Important!
                        messages.success(
                            request, 'Your password was successfully updated!')
                        return redirect('user-Profile')
                    else:
                        messages.error(request, 'Please correct the error below.')
                else:
                    form = passwordform(request.user)
                context = {
                    'form': form
                    }
                return render(request,'Store_manager/profile/chage_pass.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def chage_profile_pic(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
                users = User.objects.get(id=request.user.id)
                re_employ=employ.objects.get(user=users)
                admin = re_employ
                context= {
                    'admin':admin,
                    're_emp':admin,
                }
                if len(request.FILES.get('newimg', "")) != 0:
                    
                    admin.profile_pic.delete()
                    admin.profile_pic = request.FILES.get('newimg', "")
                    admin.save()
                    messages.success(request,'Your profile picture has been updated successfully.')
                    return redirect('user-Profile')
                else:
                    return render(request,'Store_manager/profile/change_profile_pic.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def delete_profile_pic(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
                users = User.objects.get(id=request.user.id)
                re_employ=employ.objects.get(user=users)
                admin = re_employ
                context= {
                    'admin':admin,
                    're_emp':admin,
                }
                if len(admin.profile_pic) != 0:
                    admin.profile_pic.delete()
                    return redirect('user-Profile')
                return render(request,)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  

def purchase(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
              return render(request,'Store_manager/for_purchase/purchase.html')
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
    


def new_action1(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            if form1temp.objects.all().count() !=0:
                    all_form= form1temp.objects.all()
                    form1=all_form[0]
                    form1temp.objects.all().delete()
                    if request.method == 'POST':
                        Request_by=request.POST.get('Request_by')
                        Department=request.POST.get('Department')
                        checked_by=request.POST.get('checkd_by')
                        approved_by=request.POST.get('Approved_by')
                        form1=form1temp.objects.create(Request_by=Request_by,Department=Department,checkd_by=checked_by, Approved_by=approved_by)
                        if form1:
                            messages.success(request,'You have sumite Form-1 successfuly.')
                            return redirect('purchase')
                    else:
                        if request.method == 'POST':
                            Request_by=request.POST.get('Request_by')
                            Department=request.POST.get('Department')
                            checked_by=request.POST.get('checkd_by')
                            approved_by=request.POST.get('Approved_by')
                            form1=form1temp.objects.create(Request_by=Request_by,Department=Department,checkd_by=checked_by, Approved_by=approved_by)
                            if form1:
                                messages.success(request,'You have sumite Form-1 successfuly.')
                                return redirect('purchase')
                    return render(request,'Store_manager/for_purchase/purchase.html')
    
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   

def new_action(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            if request.method == 'POST':
                all_form= form1temp.objects.all()
                if all_form:
                    form1=all_form[0]
                    des=request.POST.get('desc')
                    Qty=request.POST.get('qty')
                    unit=request.POST.get('unit')
                    remark=request.POST.get('remark')
                    form2=form2temp.objects.create(form1=form1,Description=des,unit=unit,req_qty=Qty,Remark=remark)
                    if form2:
                        messages.success(request,'You have sumite Form-2 successfuly.')
                        return redirect('purchase')
                else:
                    messages.error(request,'First, you must complete and submit Form 1')
                    return redirect('purchase')
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  
def check_out(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            all_form= form1temp.objects.all()
            if all_form:
                form1=all_form[0]
                all_item=form2temp.objects.filter(form1=form1)
                if all_item:
                    context={
                        'form1':form1,
                        'all_item':all_item,
                        're_emp':re_emp
                    }
                    return render(request,'Store_manager/for_purchase/check_out.html',context)
                else:
                    messages.error(request,'First, you must complete and submit Form 2. ')
            else:
                messages.error(request,'First, you must complete and submit Form 1. ')
            return render(request,'Store_manager/for_purchase/purchase.html')

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def list_for_purchase(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            all_list_item=form2permanent.objects.all().order_by('-id')
            context={
                're_emp':re_emp,
                'all_list_item':all_list_item,
            }
            all_form= form1temp.objects.all()
            if all_form:
                form1=all_form[0]
                all_item=form2temp.objects.filter(form1=form1)
                Request_by=form1.Request_by
                Department=form1.Department
                checkd_by=form1.checkd_by
                Approved_by=form1.Approved_by
                form1per=form1permanent.objects.create(Request_by=Request_by,Department=Department,checkd_by=checkd_by,Approved_by=Approved_by)
                if form1per:
                    for item in all_item:
                        Description=item.Description
                        unit=item.unit
                        qty=item.req_qty
                        Remark=item.Remark
                        form2permanent.objects.create(form1per=form1per,Description=Description,unit=unit,req_qty=qty,Remark=Remark)
                        # messages.success(request,'You have submitted your purchase request successfully.')
                        form1temp.objects.all().delete()
                    messages.success(request,'You have submitted your purchase request successfully.')
                        
            return render(request,'Store_manager/for_purchase/purchase_list.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  

# ------------------------------ chat ---------------------------------------
def chat(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
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
                    're_emp':re_emp,
                }
                return render(request,'Store_manager/chat/index1.html',context)

            context={
                    'chat_group':all_chate_team,
                    'admin':admin,
                    'my_message':my_message,
                    're_emp':re_emp,
                }
            return render(request,'Store_manager/chat/index.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def store_all_user(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
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
                're_emp':re_emp
            }
            return render(request,'Store_manager/chat/index2.html',context)
    
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    

def chat_pepol(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
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
                    return redirect('chat_pepol',id)
            context={
                'chat_employ':chat_employ,
                'message':all_message,
                'id':id,
                'me':me,
                're_emp':re_emp,
            }
            return render(request,'Store_manager/chat/chat.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  
def chat_profile(request,id):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            chat_employ=employ.objects.get(pk=id)
            context={
                'chat_employ':chat_employ,
                're_emp':re_emp,
            }
            return render(request,'Store_manager/chat/profile.html',context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
def send_message(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':

            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            me=request.user
            if request.method == 'POST':
                pass
            return redirect('chat_pepol')
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   


# --------------------------------- End Chat ----------------------------------

def report(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':

                return render(request,'Store_manager/Report/index.html',)
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    



def add_to_store(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            id=(request.user.id)
            user=User.objects.get(id=id)
            re_emp=employ.objects.get(user=user)
            re_Store=allStore.objects.get(storeKeeper=re_emp.Full_Name)
            try:
                all_catagory = Catagory.objects.filter(store=re_Store)
            except Catagory.DoesNotExist:
                all_catagory = None
            
            context ={
                'all_catagory':all_catagory,
                're_emp':re_emp,
                
            }
            if request.method == 'POST':
                Reseaon = request.POST.get('res')
                if (Reseaon=='Gift'):
                    pass
                elif (Reseaon=='Purchased'):
                    OrderId= request.POST.get('OrderId')
                    item_name= request.POST.get('item_name')
                    Qty= int(request.POST.get('Qty'))
                    catagory= request.POST.get('catagory_name')

                    item=form2permanent.objects.get(id=OrderId)
                    check=Item.objects.filter(item_name=item_name)
                    if (item.Admin_Appruval == 'Approved' ):
                        if (item.Finance_Action == 'Completed'):
                            item.add_qty=item.add_qty+Qty
                            if (item.req_qty-item.add_qty==0):
                                item.Item_Status="Completed"
                                cat=Catagory.objects.get(Catagory_Name=catagory)
                                check=Item.objects.filter(item_name=item_name)
                                if check.count():
                                    add_item=Item.objects.get(item_name=item_name)
                                    add_item.total_item_in_Stok = str(item.add_qty)
                                    ItemHistory.objects.create(Item=add_item,Reason='Purchased',Amount=item.add_qty,Action='Add')
                                    add_item.save()
                                else:
                                    new_item=Item.objects.create(
                                    store=re_Store,
                                    Catagory=cat,
                                    Order_Id=OrderId,
                                    item_name=item_name,
                                    Reason='Purchased',
                                    total_item_in_Stok= item.add_qty,
                                    add_by=re_emp,
                                    Action='New_Add',
                                    )
                                    if new_item:
                                        ItemHistory.objects.create(Item=new_item,Reason='Purchased',Amount=item.add_qty,Action='Add')
                                    
                            
                            elif(item.req_qty>item.add_qty):
                                item.Item_Status="Pending"
                                if check.count():
                                    add_item=Item.objects.get(item_name=item_name)
                                    add_item.total_item_in_Stok = str(item.add_qty)
                                    ItemHistory.objects.create(Item=add_item,Reason='Purchased',Amount=item.add_qty,Action='Add')
                                    add_item.save()
                                else:
                                    new_item=Item.objects.create(
                                    store=re_Store,
                                    Catagory=cat,
                                    Order_Id=OrderId,
                                    item_name=item_name,
                                    Reason='Purchased',
                                    total_item_in_Stok= item.add_qty,
                                    add_by=re_emp,
                                    Action='New_Add',
                                    )
                                    if new_item:
                                        ItemHistory.objects.create(Item=new_item,Reason='Purchased',Amount=item.add_qty,Action='Add')
                                    
                            elif(item.req_qty<item.add_qty):
                                item.add_qty=item.add_qty-Qty
                                messages.error(request,'Sorry, the data you entered is not valid.')
                                return redirect('list_for_purchase')
                            item.save()
                        
                        else:
                            messages.error(request,'The request was not completed by Finance.') 
                    else:
                        messages.error(request,'The request was not approved by the Administrator.')       
                elif (Reseaon=='Other'):
                    pass
                elif (Reseaon=='Returned'):
                    pass
            
                return redirect('list_for_purchase')
            return render(request,"Store_manager/Add_to_Store/add_to_store.html",context)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
def add_to_store_by_return(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            user_id=(request.user.id)
            user=User.objects.get(id=user_id)
            re_emp=employ.objects.get(user=user)
            if request.method == 'POST':
                name_id=int(str(request.POST.get('name')))
                Description=str(request.POST.get('item'))
                qty=int(str(request.POST.get('qty')))
            req_item_inlower=Description.lower()
            req_item_inupper=Description.capitalize()
            try: 
                ret_item=Item.objects.get(item_name=req_item_inlower)
            except:
                try:
                    ret_item=Item.objects.get(item_name=req_item_inupper)
                except ObjectDoesNotExist:
                    ret_item=None
            ret_emp=employ.objects.get(id=name_id)
            Request_by=ret_emp.Full_Name
            
            current_instok=int(ret_item.total_item_in_Stok)
            updated=current_instok + qty
            returend_item=employe_request_form1_permanent.objects.get(Q(Request_by=Request_by) & Q(Description=Description))
            request_qty=int(str(returend_item.req_qty))
            if request_qty == qty: 
                ret_item.total_item_in_Stok=str(updated)
                returend_item.Recival_status_by_Employer='Returned'
                ItemHistory.objects.create(Item=ret_item,Reason='Returned Material',Action='Add',Amount=qty,return_by=Request_by)
                
            elif request_qty > qty:
                ret_item.total_item_in_Stok=str(updated)
                after_ret=request_qty-qty
                returend_item.req_qty=str(after_ret)
                ItemHistory.objects.create(Item=ret_item,Reason='Returned Material',Action='Add',Amount=qty,return_by=Request_by)
            else : 
                messages.error(request,'Please enter valid data.')
                return redirect('add-to-store1')
            returend_item.save()
            ret_item.save()
            return redirect('item_detail', ret_item.id)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
  
 
def add_to_store_by_gift(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            if request.method == 'POST':
                    gifted_by=request.POST.get('gifted_by')
                    item_name=request.POST.get('item')
                    amount=request.POST.get('amount')
                    qty=int(str(amount))
                    ret_item=Item.objects.get(item_name=item_name)
                    current_instok=int(ret_item.total_item_in_Stok)
                    updated=current_instok + qty
                    ret_item.total_item_in_Stok=str(updated)
                    ret_item.save()
                    ItemHistory.objects.create(Item=ret_item,Reason='Gift',Action='Add',Amount=amount,gift_by=gifted_by)
                    return redirect('item_detail', ret_item.id)

   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')

    
def add_to_store_by_other(request):
    try:
        if request.user.groups.all()[0].name == 'Store_Manager':
            if request.method == 'POST':
                reseaon=request.POST.get('reseaon')
                item_name=request.POST.get('item')
                amount=request.POST.get('amount')
                qty=int(str(amount))
                ret_item=Item.objects.get(item_name=item_name)
                current_instok=int(ret_item.total_item_in_Stok)
                updated=current_instok + qty
                ret_item.total_item_in_Stok=str(updated)
                ret_item.save()
                ItemHistory.objects.create(Item=ret_item,Reason='Other',Action='Add',Amount=amount,Other_Reseaon=reseaon)
            
            return redirect('item_detail', ret_item.id)
   
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
   
class GeneratePdf(View):
   def get(self, request, *args, **kwargs):
    all_form= form1temp.objects.all()
    if all_form:
        form1=all_form[0]
        all_item=form2temp.objects.filter(form1=form1)
        data={
            'form1':form1,
            'all_item':all_item,
        }
        open('templates/temp.html', "w").write(render_to_string('Store_manager/for_purchase/invoce.html',data ))
        pdf = html_to_pdf('temp.html')
    return HttpResponse(pdf, content_type='application/pdf')



class deliverd_item(View):
   def get(self, request,id, *args, **kwargs,):
    item=employe_request_form1_permanent.objects.get(id=id)
    Department=item.Department
    re_dep=department.objects.get(departmentName=Department)
    dep_head=re_dep.departmentHead
    req=item.Request_by
    req_em=employ.objects.get(Full_Name=req)
    data={
        'item':item,
        'req_em':req_em,
        'dep_head':dep_head,
    }
    open('templates/temp.html', "w").write(render_to_string('Store_manager/cheeck_Request/pdf_format_to delivered.html',data ))
    pdf = html_to_pdf('temp.html')
    return HttpResponse(pdf, content_type='application/pdf')