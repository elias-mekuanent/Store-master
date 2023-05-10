from django.urls import path
from .import views

urlpatterns = [
    path('admin-dashboard', views.home, name='admin-dashboard'),
    path('deparetment-dashboard', views.deparetment_dashboard, name='deparetment-dashboard'),
    path('employees-dashboard', views.employees_dashboard, name='employees-dashboard'),
    path('users-profile',views.user_profile,name='users-profile'),
 
    # MANAGE EMPLOYEE
    path('manage-employee', views.manage_employee, name='manage-employee'),
    
    path('item_in_employee/<int:id>',views.item_in_employee, name='item_in_employee'),

    # DEPARTMENT
    path('departments', views.departments, name='departments'),
    path('department-details/<int:id>',views.item_in_each_department,name='department-details'),
    path('set_dept_head',views.set_dept_head,name='set_dept_head'),
    

    # Vendors
    path('vendors', views.vendors, name='vendors'),
    path('add-new-vendor',views.add_new_vendor,name='add-new-vendor'),
    path('vendor-detail/<int:id>', views.vendor_detail, name='vendor-detail'),

    
    # Role
    path('role', views.role, name='role'),
    

    # Store
    path('store', views.store, name='store'),
    path('store-details/<int:id>', views.store_details, name='store-details'),
    path('delete-store/<int:id>', views.delete_store, name='delete-store'),
    path('store_manager_update/<int:id>', views.store_manager_update, name='store_manager_update'),
    
    path('add-new-store',views.add_new_store,name='add-new-store'),
    path('cat-item-detail/<int:id>',views.cat_item_detail,name='cat-item-detail'),
    path('department-delete/<int:id>',views.department_delete,name='department-delete'),

    # 
    
    path('purchase_item', views.Purchase_item, name='Purchase_item'),
    path('admin_respons/<int:id>', views.admin_respons, name='admin_respons'),
    

  # -------- Chat --------- #
    path('chat/',views.chat,name="admin-chat"),
    path('chat_pepol/<int:id>',views.chat_pepol,name="admin-chat_people"),

    path('chat_profile/<int:id>',views.chat_profile,name="admin-chat_profile"),
    path('send_message/',views.send_message,name="new"),
   
   # -------- End Chat --------- #
]