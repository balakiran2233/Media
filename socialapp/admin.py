
from django.contrib import admin
from .models import Article,Comment

class AdminArticle(admin.ModelAdmin):
    list_display=['title','slug','author','created_date','body']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Article,AdminArticle)
admin.site.register(Comment)


#admin 12345
#sivaprasad 123456
#Ramyamounika sivaprasad12
#rakul ABCD8899
#keerthisuresh ZYX1122
