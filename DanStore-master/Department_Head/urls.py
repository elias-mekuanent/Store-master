from django.urls import path
from .import views
urlpatterns = [
   path('',views.dept_head,name="dept-dashboard"),
   path('add_employe',views.add_employe,name="add_employe"),
   path('check_request',views.cheek_request,name="check_request"),
   path('add_emp',views.add_emp,name="add_emp"),
   path('dept_approved/<int:id>',views.dept_approved,name="aprove_request"),
   path('dept_reject/<int:id>',views.dept_reject,name="reject_request"),
   path('unreceived-request',views.unreceived_request,name="unreceived-request"),
   path('rejected_emp_request',views.rejected_emp_request,name="rejected_emp_request"),
   path('make_request',views.dept_request,name="make_request"),
   path('dpte_request2',views.dept_request2,name="dept_request2"),
   path('dept_complet_request',views.dept_complet_request,name="dept_complet_request"),
   path('all_item_taken_by',views.all_item_taken_by,name="all_item_taken_by"),

   # ---------------------- chat ------------------------------------------
   path('dept_chat/',views.dept_chat,name="dept_chat"),
   path('dept_chat_pepol/<int:id>',views.dept_chat_pepol,name="dept_chat_pepol"),
   path('dept_chat_profile/<int:id>',views.dept_chat_profile,name="dept_chat_profile"),
   path('all_user/',views.all_user,name="all_user"),
   path('dept_check_mess/<int:id>',views.dept_check_mess,name="dept_check_mess"),
   
   # ---------------------- End Chat ---------------------------------------
   path('dept_role',views.role,name="dept_role"),
   
    # -------- profile --------- #
   path('dept_user_Profile',views.user_Profile,name="dept_user-Profile"),
   path('emp_edit_Profile',views.edit_Profile,name="emp_edit-Profile"),
   path('emp_chage_password',views.chage_password,name="emp_chage_password"),
   path('emp_pp',views.emp_chage_profile_pic,name="emp_pp"),
   path('emp_delete_pic',views.delete_profile_pic,name="emp_delete-pic"),
   # -------- End profile --------- #


   
    
]