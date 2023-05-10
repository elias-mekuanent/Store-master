
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("account.urls") ),
    path('comp-admin/',include("Company_Admin.urls")),
    path('Store_Manager/',include("Store_manager.urls")),
    path('department_head/',include("Department_Head.urls")),
    path('Employer/',include("Employer.urls")),
    path('Finance/',include("Finance.urls")),
    path('Human_Resource/',include("human_resource.urls")),

    
    

    
    
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
