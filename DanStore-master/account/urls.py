from django.urls import path
from .import views
urlpatterns = [
   path('',views.login_view,name="login"),
   path('registration_form1',views.registration_form1,name="registration-form1"),
   path('registration_form2',views.registration_form2,name="registration-form2"),
   path('registration_form3',views.registration_form3,name="registration-form3"),
   path('thanks',views.registration_final,name="thanks"),
   path('log_out',views.logout_view,name="log-out"),
   
]
