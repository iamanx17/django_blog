from django.contrib import admin
from django.urls import path,include


#customizing admin section 
admin.site.site_header='Pirates venture administration'
admin.site.site_title='Admin'
admin.site.index_title='Welcome to pirates venture'
#------xxxx-----



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('account/',include('account.urls')),   
   ]
