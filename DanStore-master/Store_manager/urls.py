from django.urls import path
from .import views
from .views import GeneratePdf,deliverd_item


urlpatterns = [
   path('pdf/', GeneratePdf.as_view(),name="pdf"),
   path('pdf_to_deliverd_item/<int:id>', deliverd_item.as_view(),name="dilverd_item"),
   path('',views.store_dashboard,name="store-dashboard"),
        
   # 
   # -------- profile --------- #
   path('user_Profile',views.user_Profile,name="user-Profile"),
   path('edit_Profile',views.edit_Profile,name="edit-Profile"),
   path('chage_password',views.chage_password,name="chage_password"),
   path('chage_profile_pic',views.chage_profile_pic,name="chage-profile-pic"),
   path('delete_pic',views.delete_profile_pic,name="delete-pic"),
   # -------- End profile --------- #

   path('add_to_store',views.add_to_store,name="add-to-store"),
   path('add_to_store_by_return',views.add_to_store_by_return,name="add-to-store-by-return"),
   path('add_to_store_by_gift',views.add_to_store_by_gift,name="add-to-store-by-gift"),
   path('add_to_store_by_other',views.add_to_store_by_other,name="add_to_store_by_other"),
        
   path('add_to_store1',views.add_to_store1,name="add-to-store1"),
   path('cheek_request',views.cheeck_request,name="cheeck-request"),
   path('aproved_request',views.aproved_request,name="aproved_request"),
   path('Item_Delivery_form/<int:id>',views.Item_Delivery_form,name="Item_Delivery_form"),
   path('set_item_specifications/<int:id>',views.set_item_specifications,name="set_item_specifications"),
   path('check_delivered_item/<int:id>',views.check_delivered_item,name="check_delivered_item"),
   path('rejected-request',views.rejected_request,name="rejected-request"),
   path('check-in-stok/<str:Description>',views.check_in_stok,name="check-in-stok"),
   
   path('meassge_to_reject/<int:id>',views.put_message_rejected_request,name="message_to_reject"),
   path('send_message_req/<int:id>',views.send_message_to_request,name="send-message-req"),
   path('store_manage_approve',views.store_manage_approve,name="store-manage-approve"),
  
   
   # ---------- Catagory ---------- #
   path('manage_catagory/',views.manage_catagory,name="manage-catagory"),
   path('search_catagory/',views.search_catagory,name="search-catagory"),
   path('add_new_catagory',views.add_new_catagory,name="new-catagory"),
   path('catagory_detail/<int:id>',views.catagory_detail,name="catagory-detail"),
   path('catagory_delete/<int:id>',views.delete_catagory,name="catagory-delete"),
   path('item_detail/<int:id>',views.item_detail,name="item_detail"),
   path('item_delete/<int:id>',views.item_delete,name="item-delete"),
   path('add_item/<int:id>',views.add_item,name="add-item"),

   # -------- End Catagory --------- #


   # ---------- Purchase ------------ #
   path('purchase/',views.purchase,name="purchase"),
   path('list_for_purchase/',views.list_for_purchase,name="list_for_purchase"),
   path('check_out/',views.check_out,name="check-out"),
   path('new_action1/',views.new_action1,name="new_action1"),
   path('new_action/',views.new_action,name="new_action"),

   # -------- End Purchase --------- #

   # -------- Chat --------- #
   path('chat/',views.chat,name="chat"),
   path('st_all_user/',views.store_all_user,name="st-all-user"),
   path('chat_pepol/<int:id>',views.chat_pepol,name="chat_pepol"),
   path('chat_profile/<int:id>',views.chat_profile,name="chat_profile"),
   path('send_message/',views.send_message,name="new"),


   
   # -------- End Chat --------- #

   # -------- Report --------- #
   path('report/',views.report,name="report"),
   # -------- End Report --------- #
]
