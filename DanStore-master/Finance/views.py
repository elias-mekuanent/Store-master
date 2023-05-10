from django.shortcuts import render,redirect
from django.contrib import messages
from Store_manager.models import *
def finance_view(request):
    try:
        if request.user.groups.all()[0].name == 'Finance':
            all_list_item=form2permanent.objects.all()
            context={
                'all_list_item':all_list_item,
            }
            return render(request,'Finance/index.html',context)
        
        messages.error(request, 'Permission denied ')
        return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    
    
def finance_respons(request,id):
    try:
            if request.user.groups.all()[0].name == 'Finance':
                    req_order=form2permanent.objects.get(pk=id)
                    context={
                    'req_order':req_order,
                     }
                    if 'approve' in request.POST:
                        note=request.POST.get('note')
                        req_order.Finance_response=note
                        req_order.Finance_Action='Completed'
                        req_order.save()
                        return redirect('finance_dashboard')

                    return render(request,'Finance/finance_respons.html',context)
            
            messages.error(request, 'Permission denied ')
            return redirect('log-out')
    except IndexError as e:
        messages.error(request, 'Login Before ')
        return redirect('log-out')
    