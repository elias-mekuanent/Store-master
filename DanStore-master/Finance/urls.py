from django.urls import path
from .import views
urlpatterns = [
   path('',views.finance_view,name="finance_dashboard"),
   path('finance_respons/<int:id>', views.finance_respons, name='finance_respons'),
    
        
]