from django.contrib import admin
from .models import blogpost,comment,usermessage,newsletter

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=['title','status','created_on']
    list_filter=['title','author']
    search_fields=['title','slug','content']
    prepopulated_fields={'slug':['title']}
    raw_id_fields=['author']  

    class Media:        
        css={
            "all":('css/admin.css',)
        }
        js=("js/editor.js",)


class commentAdmin(admin.ModelAdmin):
    list_display=['user','cmt_content']
    list_filter=['date','user']
    search_fields=['cmt_content','post']


class projectsAdmin(admin.ModelAdmin):
    list_display=['id','title','desc','img','date']
    list_filter=['title','desc']
    search_fields=['title']

class usermessageAdmin(admin.ModelAdmin):
    list_display=['id','email','date']
    list_filter=['date']
    search_fields=['email','msg']

class newsletterAdmin(admin.ModelAdmin):
    list_display=['id','email','date']
    list_filter=['date']
    search_fields=['email']



admin.site.register(blogpost,BlogAdmin)
admin.site.register(comment,commentAdmin)
admin.site.register(usermessage,usermessageAdmin)
admin.site.register(newsletter,newsletterAdmin)