from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Usernew,Post,Comment,Category

#admin.site.register(Usernew)
#admin.site.register(Post)
#admin.site.register(Comment)
#admin.site.register(Category)

class UsernewAdmin(admin.ModelAdmin):
  list_display = ("ID_Usernew", "Username","Email","Password")
admin.site.register(Usernew, UsernewAdmin)

class PostAdmin(admin.ModelAdmin):
  list_display = ("ID_Post","Title","Content","Category","Date_Published")
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
  list_display = ("ID_Comment","Post_ID","User_ID","Content","Date_Posted")
admin.site.register(Comment, CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('ID_Category','Name')
admin.site.register(Category, CategoryAdmin)




