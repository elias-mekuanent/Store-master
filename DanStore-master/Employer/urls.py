from django.urls import path
from .import views
from .views import emp_deliverd_item
    
urlpatterns = [
   path('emp_pdf_to_deliverd_item/<int:id>', emp_deliverd_item.as_view(),name="emp_dilverd_item"),
   path('',views.employe_view,name="employe_dashboard"),
   path('emp_request',views.emp_request,name="emp_request"),
   path('emp_request2',views.emp_request2,name="emp_request2"),
   path('complet_request',views.complet_request,name="complet_request"),
   path('reste_request_form',views.reste_request_form,name="reste_request_form"),
   path('view_request/<int:id>',views.view_request,name="view_request"),
   path('approved_accept/<int:id>',views.accept_approveal,name="approved_accept"),  
   path('cancel_request/<int:id>',views.cancel_request,name="cancel_request"),
        
   path('pending_item',views.pending_item,name="pending_item"),
   path('total_item_in_me',views.total_item_in_me,name="total_item_in_me"),
   path('Returned_item',views.Returned_item,name="Returned_item"),
   path('Rejected_Canceld',views.Rejected_Canceld,name="Rejected_Canceld"),
        
        
  # -------- profile --------- #
   path('emp_user_Profile',views.user_Profile,name="emp_user-Profile"),
   path('emp_edit_Profile',views.edit_Profile,name="emp_edit-Profile"),
   path('emp_chage_password',views.chage_password,name="emp_chage_password"),
   path('emp_pp',views.emp_chage_profile_pic,name="emp_pp"),
   path('emp_delete_pic',views.delete_profile_pic,name="emp_delete-pic"),
   # -------- End profile --------- #
    
]